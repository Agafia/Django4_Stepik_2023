# В manage.py shell или отдельном скрипте
import redis

try:
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    r.ping()
    print("Redis connection successful!")
except redis.ConnectionError:
    print("Redis connection failed!")