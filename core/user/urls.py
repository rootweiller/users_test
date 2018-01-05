from django.contrib import admin
from django.urls import path
from .views import UsersAPI

urlpatterns = [
    path('API/V1/list_all', UsersAPI.as_view(), name="UsersAPI"),
]
