import sqlalchemy as sa

from sendify.alembic_models.carrier_db_result import CarrierDbResult
from sendify.alembic_models.product_db_result import ProductDbResult
from sendify.alembic_models.transit_time_db_result import TransitTimeDbResult

meta = sa.MetaData()

carrier = sa.Table(
    'Carriers', meta,
    sa.Column('carrier_id', sa.Integer, primary_key=True),
    sa.Column('carrier_name', sa.TEXT),
    sa.Column('price_per_km', sa.REAL),
    sa.Column('price_per_kg', sa.REAL),

)

transit_time = sa.Table(
    'Expected_transit_time', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('origin_city', sa.TEXT),
    sa.Column('destination_city', sa.TEXT),
    sa.Column('transit_time', sa.TEXT),
    sa.Column('distance', sa.Integer),
    sa.Column('carrier_id', sa.Integer, None, sa.ForeignKey('carrier.carrier_id')),

)

products = sa.Table(
    'Products', meta,
    sa.Column('product_id', sa.Integer, primary_key=True),
    sa.Column('product_type', sa.TEXT),
    sa.Column('def_weight', sa.REAL),
    sa.Column('def_width', sa.REAL),
    sa.Column('def_height', sa.REAL),
    sa.Column('def_length', sa.REAL),

)


async def get_carrier(postgres, carrier_id):
    carrier_db_obj = CarrierDbResult()
    query = (sa.select([carrier], use_labels=True).where(carrier.c.carrier_id == carrier_id))

    async for row in postgres.execute(query):
        carrier_db_obj.carrier_name = row.Carriers_carrier_name
        carrier_db_obj.price_per_km = row.Carriers_price_per_km
        carrier_db_obj.price_per_kg = row.Carriers_price_per_kg

    return carrier_db_obj


async def get_product(postgres, product_type):
    product_db_obj = ProductDbResult()
    query = (sa.select([products], use_labels=True).where(products.c.product_type == product_type))

    async for row in postgres.execute(query):
        product_db_obj.def_weight = row.Products_def_weight
        product_db_obj.def_width = row.Products_def_width
        product_db_obj.def_height = row.Products_def_height
        product_db_obj.def_length = row.Products_def_length

    return product_db_obj


async def get_transit_time(postgres, origin_city, destination_city):
    res = list()
    query = (sa.select([transit_time], use_labels=True).where(
        transit_time.c.origin_city == origin_city and transit_time.c.destination_city == destination_city
    ))

    async for row in postgres.execute(query):
        transit_time_obj = TransitTimeDbResult()
        transit_time_obj.transit_time = row.Expected_transit_time_transit_time
        transit_time_obj.distance = row.Expected_transit_time_distance
        transit_time_obj.carrier_id = row.Expected_transit_time_carrier_id

        res.append(transit_time_obj)

    return res
