from aiohttp import web
from sendify.database import get_carrier


async def index(request):
    return web.Response(text='Server Sendify')


async def carriers(request):
    db = request.app['db']
    carrier_name = request.headers.get("carrier")

    async with db.acquire() as conn:
        carriers = await get_carrier(conn, carrier_name)

        result = {
            "carriers": carriers
        }

    return web.json_response(result)