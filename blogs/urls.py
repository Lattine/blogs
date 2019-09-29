from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("article/", include("article.urls", namespace="article")),
    path("user/", include("user.urls", namespace="user")),
]
