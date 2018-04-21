import sqlalchemy as sa

from sendify.alembic_models.carrier_db_result import CarrierDbResult
from sendify.alembic_models.product_db_result import ProductDbResult
from sendify.alembic_models.transit_time_db_result import TransitTimeDbResult
from sendify.support.db_data.data import CARRIERS_DATA, PRODUCTS_DATA, EXPECTED_TIME_DATA

meta = sa.MetaData()

carrier = sa.Table(
    'carriers', meta,
    sa.Column('carrier_id', sa.Integer, primary_key=True),
    sa.Column('carrier_name', sa.TEXT),
    sa.Column('price_per_km', sa.REAL),
    sa.Column('price_per_kg', sa.REAL),

)

expected_transit_time = sa.Table(
    'expected_transit_time', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('origin_city', sa.TEXT),
    sa.Column('destination_city', sa.TEXT),
    sa.Column('transit_time', sa.TEXT),
    sa.Column('distance', sa.Integer),
    sa.Column('carrier_id', sa.Integer, None, sa.ForeignKey('carrier.carrier_id')),

)

products = sa.Table(
    'products', meta,
    sa.Column('product_id', sa.Integer, primary_key=True),
    sa.Column('product_type', sa.TEXT),
    sa.Column('def_weight', sa.REAL),
    sa.Column('def_width', sa.REAL),
    sa.Column('def_height', sa.REAL),
    sa.Column('def_length', sa.REAL),

)


async def create_tables(conn):
    await conn.execute('DROP TABLE IF EXISTS carriers CASCADE')
    await conn.execute('DROP TABLE IF EXISTS expected_transit_time')
    await conn.execute('DROP TABLE IF EXISTS products')
    await conn.execute('''CREATE TABLE carriers (
                                        carrier_id serial PRIMARY KEY,
                                        carrier_name varchar(253),
                                        price_per_km float,
                                        price_per_kg float)''')

    await conn.execute('''CREATE TABLE expected_transit_time (
                                id serial PRIMARY KEY,
                                origin_city varchar(253),
                                destination_city varchar(253),
                                transit_time varchar(253),
                                distance int,
                                carrier_id serial references carriers(carrier_id))''')

    await conn.execute('''CREATE TABLE products (
                                            product_id serial PRIMARY KEY,
                                            product_type varchar(253),
                                            def_weight float,
                                            def_width float,
                                            def_height float,
                                            def_length float)''')


async def fill_data(conn):
    async with conn.begin():
        for carrier_id, data in CARRIERS_DATA.items():
            await conn.execute(carrier.insert().values(
                carrier_id=carrier_id,
                carrier_name=data.get('carrier_name'),
                price_per_km=data.get('price_per_km'),
                price_per_kg=data.get('price_per_kg')))

        for product_id, data in PRODUCTS_DATA.items():
            await conn.execute(products.insert().values(
                product_id=product_id,
                product_type=data.get('product_type'),
                def_weight=data.get('def_weight'),
                def_width=data.get('def_width'),
                def_height=data.get('def_height'),
                def_length=data.get('def_length')
            ))

        for id, data in EXPECTED_TIME_DATA.items():
            await conn.execute(expected_transit_time.insert().values(
                id=id,
                origin_city=data.get('origin_city'),
                destination_city=data.get('destination_city'),
                transit_time=data.get('transit_time'),
                carrier_id=data.get('carrier_id'),
                distance=data.get('distance')
            ))
    return True


async def get_carrier(postgres, carrier_id):
    carrier_db_obj = CarrierDbResult()
    query = (sa.select([carrier], use_labels=True).where(carrier.c.carrier_id == carrier_id))

    async for row in postgres.execute(query):
        carrier_db_obj.carrier_name = row.carriers_carrier_name
        carrier_db_obj.price_per_km = row.carriers_price_per_km
        carrier_db_obj.price_per_kg = row.carriers_price_per_kg

    return carrier_db_obj


async def get_product(postgres, product_type):
    product_db_obj = ProductDbResult()
    query = (sa.select([products], use_labels=True).where(products.c.product_type == product_type))

    async for row in postgres.execute(query):
        product_db_obj.def_weight = row.products_def_weight
        product_db_obj.def_width = row.products_def_width
        product_db_obj.def_height = row.products_def_height
        product_db_obj.def_length = row.products_def_length

    return product_db_obj


async def get_transit_time(postgres, origin_city, destination_city, log):
    res = list()

    query = (sa.select([expected_transit_time], use_labels=True).where(
        expected_transit_time.c.origin_city == origin_city).where(
        expected_transit_time.c.destination_city == destination_city
    ))

    async for row in postgres.execute(query):
        transit_time_obj = TransitTimeDbResult()
        transit_time_obj.transit_time = row.expected_transit_time_transit_time
        transit_time_obj.distance = row.expected_transit_time_distance
        transit_time_obj.carrier_id = row.expected_transit_time_carrier_id

        res.append(transit_time_obj)

    return res
