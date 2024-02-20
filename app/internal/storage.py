from app import config
import redis.asyncio as redis


async def get_redis():
    conn = redis.Redis(host=config.REDIS_HOST_NAME, port=config.REDIS_PORT)
    return conn
