import sqlalchemy as sa

meta = sa.MetaData()

carrier = sa.Table(
    'Carriers', meta,
    sa.Column('carrier_id', sa.Integer, nullable=False),
    sa.Column('carrier_name', sa.TEXT, nullable=False),
    sa.Column('price_per_km', sa.TEXT, nullable=False),
    sa.Column('price_per_kg', sa.TEXT, nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('carrier_id', name='Carriers_pkey'),
)

transit_time = sa.Table(
    'Expected_transit_time', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('origin_city', sa.TEXT, nullable=False),
    sa.Column('destination_city', sa.TEXT, nullable=False),
    sa.Column('transit_time', sa.TEXT, nullable=False),
    sa.Column('carrier_id', sa.TEXT, nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('id', name='Expected_transit_time_pkey'),
    sa.ForeignKeyConstraint(['carrier_id'], [carrier.c.carrier_id],
                            name='carrier_id',
                            ondelete='CASCADE'),
)

products = sa.Table(
    'Products', meta,
    sa.Column('product_id', sa.Integer, nullable=False),
    sa.Column('product_type', sa.TEXT, nullable=False),
    sa.Column('def_weight', sa.REAL, nullable=False),
    sa.Column('def_width', sa.REAL, nullable=False),
    sa.Column('def_height', sa.REAL, nullable=False),
    sa.Column('def_length', sa.REAL, nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('product_id', name='Products_pkey'),
)
