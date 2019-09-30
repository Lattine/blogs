from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import markdown

from .models import ArticlePost
from .forms import ArticleForm


def article_list(request):
    """文章列表页"""
    articles = ArticlePost.objects.all()  # 取出所有博客文章
    context = {'articles': articles}  # 需要传递给模板（templates）的对象
    return render(request, "article/list.html", context)  # render函数：载入模板，并返回context对象


def article_detail(request, id):
    """文章详情页"""
    article = ArticlePost.objects.get(pk=id)  # 取出相应的文章
    article.body = markdown.markdown(  # 将markdown语法渲染成html样式
        article.body,
        extensions=[
            'markdown.extensions.extra',  # 包含 缩写、表格等常用扩展
            'markdown.extensions.codehilite',  # 语法高亮扩展
        ]
    )
    context = {"article": article}  # 需要传递给模板的对象
    return render(request, "article/detail.html", context)  # 载入模板，并返回context对象


@login_required(login_url="user/login/")
def article_create(request):
    """写文章的视图"""
    if request.method == "POST":  # 判断用户是否提交数据
        article_post_form = ArticleForm(data=request.POST)  # 将提交的数据赋值到表单实例中
        if article_post_form.is_valid():  # 判断提交的数据是否满足模型的要求
            new_article = article_post_form.save(commit=False)  # 保存数据，但暂时不提交到数据库中
            new_article.author = User.objects.get(id=request.user.id)  # 指定目前登录的用户为作者
            new_article.save()  # 将新文章保存到数据库中
            return redirect("article:article_list")  # 完成后返回到文章列表，redirect可通过url地址的名字，反向解析到对应的url。
        else:
            return HttpResponse("表单内容有误，请重新填写。")  # 如果数据不合法，返回错误信息
    else:  # 如果用户请求获取数据
        article_post_form = ArticleForm()  # 创建表单类实例
        context = {"article_create_form": article_post_form}  # 需要传递给模板（templates）的对象
        return render(request, "article/create.html", context=context)  # render函数：载入模板，并返回context对象


def article_delete(request, id):
    """安全删除文章"""
    if request.method == "POST":
        article = ArticlePost.objects.get(pk=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")


def article_update(request, id):
    """更新文章"""
    article = ArticlePost.objects.get(pk=id)  # 获取需要修改的具体文章对象
    print(id, article)
    if request.method == "POST":
        article_post_form = ArticleForm(data=request.POST)  # 将提交的数据赋值到表单实例中
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id=id)  # 完成后返回到修改后的文章中。需传入文章的 id 值
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:  # 如果用户 GET 请求获取数据
        article_post_form = ArticleForm()  # 创建表单类实例
        context = {"article": article, "article_post_form": article_post_form}  # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        return render(request, "article/update.html", context)
