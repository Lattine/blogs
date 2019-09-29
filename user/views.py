from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from user.forms import UserLoginForm


def user_login(request):
    """用户登录"""
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data  # .cleaned_data 清洗出合法数据
            user = authenticate(username=data["username"], password=data["password"])  # authenticate()方法验证用户名称和密码是否匹配，如果是，则将这个用户数据返回。
            if user:
                login(request, user)  # login()方法实现用户登录，将用户数据保存在session中，即实现了登录动作
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {"form": user_login_form}
        return render(request, "userprofile/login.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_logout(request):
    """用户退出"""
    logout(request)
    return redirect("article:article_list")
