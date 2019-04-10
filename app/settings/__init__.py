from configparser import ConfigParser
from os import environ

default_config_if_error = {
    'host': '0.0.0.0',
    'port': 8080,
    'debug': True,
    'reloader': True
}

config = ConfigParser(default_config_if_error)
config.read('project_root.ini')

try:
    if environ['BOTTLE_ENVIRON'] == 'dev':
        default_config = dict(config['dev'])
    elif environ['BOTTLE_ENVIRON'] == 'prod':
        default_config = dict(config['prod'])
except KeyError:
    default_config = dict(config['test'])
