import time
from django.core.cache import cache

# class OnlineUsersMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if request.user.is_authenticated:
#             key = f'online:{request.user.id}'
#             cache.set(key, time.time(), timeout=60)  # 60 сек
#
#         return self.get_response(request)

# def get_online_users_count():
#     return len(cache.keys('online:*'))
