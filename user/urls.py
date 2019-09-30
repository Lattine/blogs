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
    path("register/", views.user_register, name="register"),
    path("delete/<int:id>/", views.user_delete, name="delete"),
    path("edit/<int:id>/", views.profile_edit, name="edit"),
]