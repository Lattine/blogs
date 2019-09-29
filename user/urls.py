# -*- coding: utf-8 -*-

# @Time    : 2019/9/29
# @Author  : Lattine

# ======================
from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]