from django.views import View
from rest_framework.generics import ListAPIView, GenericAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from article.models import Article, Channel
from article.serializers import ChannelSerializer, ArticleSerializer


class ChannelView(ListAPIView):
    #文章频道列表
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ArticleView(ListModelMixin, GenericAPIView):
    #文章列表
    serializer_class = ArticleSerializer
    def get(self,request,pk):
        if pk == '-1':
            self.queryset = Article.objects.all()
        self.queryset = Article.objects.filter(channel = pk)
        return self.list(request)

class ArticleCollectView(View):
    def put(self,request,pk):
        user = request.user
        article = Article.objects.get(id=pk)
        if user and user.is_authenticated:
            if user in article.collected_user.all():
                article.collected_users.remove(user)
                article.save()
                return Response({'success': True, 'message': '取消收藏成功'})
            article.collected_users.add(user)
            article.save()
            return Response({'success': True, 'message': '收藏成功'})
        else:
            return Response({'success':False,'message':'未登录'}, status=400)

