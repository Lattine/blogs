# -*- coding: utf-8 -*-

# @Time    : 2019/9/29
# @Author  : Lattine

# ======================
from django import forms
from .models import ArticlePost


class ArticleForm(forms.ModelForm):  # 写文章的表单类，forms.ModelForm，这个父类适合于需要直接与数据库交互的功能
    class Meta:
        model = ArticlePost  # 指明数据模型来源
        fields = ("title", "body",)  # 定义表单包含的字段
