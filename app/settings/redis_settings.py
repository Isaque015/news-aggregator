from bottle_session import SessionPlugin
from bottle_redis import RedisPlugin
from redis import ConnectionPool

plugin_session = SessionPlugin(cookie_lifetime=600)
plugin_redis = RedisPlugin()

connection_pool = ConnectionPool(host='cache', port=6379)

plugin_session.connection_pool = connection_pool
plugin_redis.redisdb = connection_pool
