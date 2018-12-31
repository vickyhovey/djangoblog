# 引入path
from django.urls import path
# 正在部署的应用的名称
# 引入views.py
from . import views
app_name = 'article'
urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
]