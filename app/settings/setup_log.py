from logging import config, getLogger

config.fileConfig('app/settings/simple_log.ini')
logger = getLogger('root')
