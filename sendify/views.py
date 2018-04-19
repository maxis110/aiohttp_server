from aiohttp import web
from sendify.database import get_carrier, get_transit_time


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

    all_res = list()
    async with db.acquire() as conn:
        transit_time_info = await get_transit_time(conn, origin_city, dest_city)

        if transit_time_info:
            for transit_time in transit_time_info:
                carrier_id = transit_time.get("carrier_id")
                expected_transit_time = transit_time.get("transit_time")

                carrier_info = await get_carrier(conn, carrier_id)

                carrier_name = None
                if carrier_info:
                    carrier_name = carrier_info.get("carrier_name")

                price = 10  #  TODO must be calculated

                result = {
                    "carrier": carrier_name,
                    "product": product_type,
                    "price": price,
                    "expected_transit_time": expected_transit_time
                }

                all_res.append(result)
    return web.json_response(all_res)
