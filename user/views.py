from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  # 引入验证登录的装饰器
from user.forms import UserLoginForm, UserRegisterForm, ProfileForm
from .models import Profile


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
        return render(request, "user/login.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_logout(request):
    """用户退出"""
    logout(request)
    return redirect("article:article_list")


def user_register(request):
    """用户注册"""
    if request.method == "POST":
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data.get("password"))  # 设置密码
            new_user.save()

            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("article:article_list")
        else:
            return HttpResponse("注册表单输入有误。请重新输入！")
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context = {"form": user_register_form}
        return render(request, "user/register.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据！")


@login_required(login_url="user/login/")
def user_delete(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        if request.user == user:  # 验证登录用户、待删除用户是否相同
            # 退出登录，删除数据并返回博客列表
            logout(request)
            user.delete()
            return redirect("article:article_list")
        else:
            return HttpResponse("你没有删除该用户的权限！")
    else:
        return HttpResponse("仅接受post请求！")


@login_required(login_url="user/login/")
def profile_edit(request, id):
    """编辑用户信息"""
    user = User.objects.get(pk=id)
    if Profile.objects.filter(user_id=id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)

    if request.method == "POST":
        if request.user != user:  # 验证修改数据者，是否为用户本人
            return HttpResponse("你没有权限修改此用户信息。")

        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile_data = profile_form.cleaned_data
            profile.phone = profile_data.get("phone")
            profile.bio = profile_data.get("bio")
            profile.save()
            return redirect("user:edit", id=id)
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == "GET":
        profile_form = ProfileForm()
        context = {"profile_form": profile_form, "profile": profile, "user": user}
        return render(request, "user/edit.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据！")
