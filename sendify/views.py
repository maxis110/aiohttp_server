from aiohttp import web

from sendify.alembic_models.headers_entry_data import HeadersEntryData
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
    headers_obj = HeadersEntryData(request)

    all_res = list()
    async with db.acquire() as conn:

        transit_time_info = await get_transit_time(conn, headers_obj.origin_city, headers_obj.destination_city)

        if transit_time_info:
            for transit_time in transit_time_info:
                carrier_id = transit_time.get("carrier_id")
                expected_transit_time = transit_time.get("transit_time")
                distance = transit_time.get("distance")

                carrier_info = await get_carrier(conn, carrier_id)

                if headers_obj.weight is None and headers_obj.width is None and \
                        headers_obj.height is None and headers_obj.length is None:

                    product_info = await get_product(conn, headers_obj.product_type)

                    headers_obj.weight = product_info.def_weight
                    headers_obj.width = product_info.def_width
                    headers_obj.height = product_info.def_height
                    headers_obj.length = product_info.def_length

                volume_of_package = get_volume_of_package(headers_obj.width, headers_obj.height, headers_obj.length)

                price = calculate_price(
                    distance,
                    volume_of_package,
                    headers_obj.weight,
                    carrier_info.price_per_kg,
                    carrier_info.price_per_km
                )

                result = {
                    "carrier": carrier_info.carrier_name,
                    "product": headers_obj.product_type,
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
