from django_redis import get_redis_connection

ONLINE_USERS_KEY = "online_users"


def get_online_users_count():
    redis = get_redis_connection("default")

    users = redis.smembers(ONLINE_USERS_KEY)
    active_users = 0

    for user_id in users:
        if redis.exists(f"online:{user_id.decode()}"):
            active_users += 1
        else:
            redis.srem(ONLINE_USERS_KEY, user_id)

    return active_users
