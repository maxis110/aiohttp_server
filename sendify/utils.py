import yaml


def load_config(file_name):
    with open(file_name, 'rt') as f:
        data = yaml.load(f)

    return data
