import uuid
from django.utils.deprecation import MiddlewareMixin
from django_redis import get_redis_connection

ONLINE_USERS_KEY = "online_users"
USER_TTL = 60


class OnlineUsersMiddleware(MiddlewareMixin):
    def process_request(self, request):
        redis = get_redis_connection("default")

        # 1️⃣ Получаем user_id
        if request.user.is_authenticated:
            user_id = f"user:{request.user.id}"
        else:
            user_id = request.COOKIES.get("anon_id")

            if not user_id:
                user_id = f"anon:{uuid.uuid4()}"
                request._set_anon_cookie = user_id

        # 2️⃣ Добавляем в SET
        redis.sadd(ONLINE_USERS_KEY, user_id)

        # 3️⃣ Обновляем TTL конкретного пользователя
        redis.setex(f"online:{user_id}", USER_TTL, 1)

    def process_response(self, request, response):
        # если это новый аноним — записываем cookie
        anon_id = getattr(request, "_set_anon_cookie", None)
        if anon_id:
            response.set_cookie(
                "anon_id",
                anon_id,
                max_age=60 * 60 * 24 * 365,
                httponly=True,
                samesite="Lax"
            )
        return response
