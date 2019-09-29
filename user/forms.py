# -*- coding: utf-8 -*-

# @Time    : 2019/9/29
# @Author  : Lattine

# ======================
from django import forms


class UserLoginForm(forms.Form):  # forms.Form，适用于不与数据库进行直接交互的功能
    username = forms.CharField()
    password = forms.CharField()
