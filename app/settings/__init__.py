from configparser import ConfigParser
from os import environ

default_confg_if_error = {
    'host': '0.0.0.0',
    'port': 8080,
    'debug': True,
    'reloader': True
}

config = ConfigParser(default_confg_if_error)
config.read('project_root.ini')

if environ['BOTTLE_ENVIRON'] == 'dev':
    default_config = dict(config['dev'])
elif environ['BOTTLE_ENVIRON'] == 'prod':
    default_config = dict(config['prod'])
else:
    default_config = dict(config['test'])
