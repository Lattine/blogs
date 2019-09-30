from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """用户扩展信息"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  # 与 User 模型构成一对一的关系

    phone = models.CharField(max_length=20, blank=True)  # 电话号码字段
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)  # 头像
    bio = models.TextField(max_length=500, blank=True)  # 个人简介

    def __str__(self):
        return "user: {}".format(self.user.username)
