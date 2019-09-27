# -*- coding: utf-8 -*-

# @Time    : 2019/9/26
# @Author  : Lattine

# ======================
from django.urls import path
from . import views

app_name = "article"  # 正在部署的应用名称

urlpatterns = [
    path("article-list/", views.article_list, name="article_list"),
    path("article-detail/<int:id>/", views.article_detail, name="article_detail"),
]
