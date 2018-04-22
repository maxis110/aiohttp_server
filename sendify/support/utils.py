import yaml

from sendify.alembic_models.db_parameters import DbParameters


def load_config(file_name):
    with open(file_name, 'rt') as f:
        data = yaml.load(f)

    return data


def parse_db_parameters(conf):
    postgres = DbParameters(conf)

    return postgres
