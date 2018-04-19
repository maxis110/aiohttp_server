from aiohttp import web

from sendify.alembic_models.headers_entry_data import HeadersEntryData
from sendify.alembic_models.shipping_proposal_result import ShippingProposalResult
from sendify.database import get_carrier, get_transit_time, get_product

FIXED_VOLUME_VALUE = 2500


async def index(request):
    return web.Response(text='Welcome to Sendify test server')


async def get_shipping_proposal(request):
    db = request.app['db']
    headers_obj = HeadersEntryData(request)

    all_res = list()
    async with db.acquire() as conn:
        transit_time_info = await get_transit_time(conn, headers_obj.origin_city, headers_obj.destination_city)

        if transit_time_info:
            for transit_time in transit_time_info:
                carrier_info = await get_carrier(conn, transit_time.carrier_id)

                await check_volume(conn, headers_obj)

                volume_of_package = get_volume_of_package(headers_obj.width, headers_obj.height, headers_obj.length)

                price = calculate_price(
                    transit_time.distance,
                    volume_of_package,
                    headers_obj.weight,
                    carrier_info.price_per_kg,
                    carrier_info.price_per_km
                )

                results = collect_proposal_results(carrier_info, headers_obj, price, transit_time)

                all_res.append(results)

    return web.json_response(all_res)


async def check_volume(conn, headers_obj):
    if headers_obj.weight is None and headers_obj.width is None and \
            headers_obj.height is None and headers_obj.length is None:
        product_info = await get_product(conn, headers_obj.product_type)

        headers_obj.weight = product_info.def_weight
        headers_obj.width = product_info.def_width
        headers_obj.height = product_info.def_height
        headers_obj.length = product_info.def_length


def collect_proposal_results(carrier_info, headers_obj, price, transit_time):
    shipping_proposal_obj = ShippingProposalResult()

    shipping_proposal_obj.carrier_name = carrier_info.carrier_name
    shipping_proposal_obj.product_type = headers_obj.product_type
    shipping_proposal_obj.price = price
    shipping_proposal_obj.expected_transit_time = transit_time.transit_time

    return shipping_proposal_obj.to_dict()


def calculate_price(distance, volume_of_package, weight, price_per_kg, price_per_km):
    if volume_of_package >= FIXED_VOLUME_VALUE:

        total_price = (price_per_kg * weight) + (price_per_km * distance)
    else:
        total_price = price_per_km * distance

    return total_price


def get_volume_of_package(width, height, length):
    return width * height * length
