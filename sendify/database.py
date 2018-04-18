import sqlalchemy as sa

meta = sa.MetaData()

carrier = sa.Table(
    'Carriers', meta,
    sa.Column('carrier_id', sa.Integer, primary_key=True),
    sa.Column('carrier_name', sa.TEXT),
    sa.Column('price_per_km', sa.TEXT),
    sa.Column('price_per_kg', sa.TEXT),

)

transit_time = sa.Table(
    'Expected_transit_time', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('origin_city', sa.TEXT),
    sa.Column('destination_city', sa.TEXT),
    sa.Column('transit_time', sa.TEXT),
    sa.Column('carrier_id', sa.TEXT, None, sa.ForeignKey('carrier.carrier_id')),

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


async def get_carrier(postgres, carrier_name):

    res = list()
    query = (sa.select([carrier], use_labels=True).where(carrier.c.carrier_name == carrier_name))

    async for row in postgres.execute(query):
        res.append(row.Carriers_carrier_name)

    return res