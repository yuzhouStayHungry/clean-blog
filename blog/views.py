from django.shortcuts import render
from django.conf import settings
from .models import *
import markdown

# Create your views here.


def index(request):

    # 分类信息获取（导航数据）
    category_list = Category.objects.all()
    # 广告数据

    # 最新文章数据
    article_list = Article.objects.all()

    # 文章归档
    # 1.先要去获取到文章中 有的 年份-月份
    # Article.objects.values('date_publish').distinct()行不通
    # Article.objects.raw('SELECT DISTINCT DATE_FORMAT(date_publish, "%%Y-%%m") as col_date FROM blog_article')

    return render(request, 'index.html', {"category_list": category_list, "article_list": article_list})


def blog_article(request, article_id):
    article = Article.object.get(id=int(article_id))
    publish_time = article.date_publish
    article.content = markdown.markdown(article.content, exteensions=[
                                'markdown.extensions.extra',
                                'markdown.extensions.codehilite',
                                'markdown.extensions.toc',
    ])
    context = {'article': article}
    return render(request, 'article.html', context)