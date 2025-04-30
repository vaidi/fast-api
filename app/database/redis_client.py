import redis
from app.config import settings

redis_client = redis.Redis.from_url(url= settings.REDIS_URL,password=settings.REDIS_PASSWORD)

def get_redis():
    return redis_client