import asyncio
import logging

import os

import sys

from aiohttp import web
from aiopg.sa import create_engine

base_module_dir = os.path.dirname(sys.modules[__name__].__file__)

try:
    import sendify  # noqa: F401 # need to check import possibility
except ImportError:
    additional_path = base_module_dir
    additional_path = os.path.join(additional_path, "..")
    sys.path.insert(0, additional_path)
    import sendify  # noqa: E402 # module level import not at top of file

from sendify.routes import setup_routes  # noqa: E402 # module level import not at top of file
from sendify.utils import load_config  # noqa: E402 # module level import not at top of file
from sendify.support.const import CONFIG_FILE  # noqa: E402 # module level import not at top of file

log = logging.getLogger(__name__)


async def main(loop):
    app = web.Application(loop=loop)

    conf = load_config(CONFIG_FILE)
    app['config'] = conf
    host, port, user, database = conf['host'], conf['port'], conf['postgres']['user'], conf['postgres']['database']

    setup_routes(app)

    app['db'] = await create_engine(
        user=user,
        database=database,
        host=host
    )

    # init logging and attach access_log
    logging.basicConfig(level=logging.DEBUG)
    app_handler = app.make_handler(access_log=log)

    srv = await loop.create_server(app_handler, host, port)
    print("Server started at http://{0}:{1}".format(host, port))
    return srv, app_handler

loop = asyncio.get_event_loop()
srv, app_handler = loop.run_until_complete(main(loop))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(app_handler.finish_connections())
    srv.close()
    loop.run_until_complete(srv.wait_closed())
loop.close()
