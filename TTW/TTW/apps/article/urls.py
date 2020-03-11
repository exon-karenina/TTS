from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from article import views

urlpatterns = [
    url(r"channels/$",views.ChannelView.as_view()),
    url(r"article/{(/)}/channel/$",views.ArticleView.as_view())
]
