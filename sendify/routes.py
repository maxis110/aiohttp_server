from sendify.views import index, get_shipping_proposal


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/proposals', get_shipping_proposal)
