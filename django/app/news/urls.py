from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('foo', views.foo),
    path('bar', views.bar),
    path('baz', views.baz),
]
