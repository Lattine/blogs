from django.shortcuts import render

import markdown

from .models import ArticlePost


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



