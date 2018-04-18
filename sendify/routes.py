from sendify.views import index, carriers


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/carriers', carriers)
