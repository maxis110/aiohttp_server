import asyncio

import os

import sys
from aiohttp import web

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


def main(loop):
    app = web.Application()

    conf = load_config(CONFIG_FILE)
    app['config'] = conf
    host, port = conf['host'], conf['port']

    setup_routes(app)
    web.run_app(app, host=host, port=port)


loop = asyncio.get_event_loop()
srv, app_handler = loop.run_until_complete(main(loop))

# if __name__ == '__main__':
#     main()
