from aiohttp import web
from sendify.database import get_carrier, get_transit_time, get_product

FIXED_VOLUME_VALUE = 2500


async def index(request):
    return web.Response(text='Server Sendify')


async def carriers(request):
    db = request.app['db']
    carrier_id = request.headers.get("carrier_id")

    async with db.acquire() as conn:
        carriers = await get_carrier(conn, carrier_id)

        result = {
            "carriers": carriers
        }

    return web.json_response(result)


async def get_shipping_proposal(request):
    db = request.app['db']
    origin_city = request.headers.get("origin_city")
    dest_city = request.headers.get("destination_city")
    product_type = request.headers.get("product_type")
    weight = request.headers.get("weight")
    width = request.headers.get("width")
    height = request.headers.get("height")
    length = request.headers.get("length")

    all_res = list()
    async with db.acquire() as conn:
        transit_time_info = await get_transit_time(conn, origin_city, dest_city)

        if transit_time_info:
            for transit_time in transit_time_info:
                carrier_id = transit_time.get("carrier_id")
                expected_transit_time = transit_time.get("transit_time")
                distance = transit_time.get("distance")

                carrier_info = await get_carrier(conn, carrier_id)

                carrier_name = None
                price_per_kg = None
                price_per_km = None
                if carrier_info:
                    carrier_name = carrier_info.get("carrier_name")
                    price_per_kg = carrier_info.get("price_per_kg")
                    price_per_km = carrier_info.get("price_per_km")

                if weight is None and width is None and height is None and length is None:
                    product_info = await get_product(conn, product_type)

                    weight = product_info.get("def_weight")
                    width = product_info.get("def_width")
                    height = product_info.get("def_height")
                    length = product_info.get("def_length")

                volume_of_package = get_volume_of_package(width, height, length)

                price = calculate_price(distance, volume_of_package, weight, price_per_kg, price_per_km)

                result = {
                    "carrier": carrier_name,
                    "product": product_type,
                    "price": price,
                    "expected_transit_time": expected_transit_time
                }

                all_res.append(result)
    return web.json_response(all_res)


def calculate_price(distance, volume_of_package, weight, price_per_kg, price_per_km):
    if volume_of_package >= FIXED_VOLUME_VALUE:

        total_price = (price_per_kg * weight) + (price_per_km * distance)
    else:
        total_price = price_per_km * distance

    return total_price


def get_volume_of_package(width, height, length):
    return width * height * length
