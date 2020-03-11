from amqp import channel
from rest_framework import serializers

from article.models import Article
from user.models import User


class ChannelSerializer(serializers.ModelSerializer):
    #频道列表
    class Meta:
        model = channel
        fields = ('id','name')




class ArticleSerializerSimple(serializers.ModelSerializer):
    #用户发表的文章
    class Meta:
        model = Article
        fields = ('id','title')

class UserSerializer(serializers.ModelSerializer):
    #文章嵌套用户序列化器
    articles = ArticleSerializerSimple(read_only =True)
    class Meta:
        model = User
        fields = ('id', 'username','avatar','articles','fans')
class ArticleSerializer(serializers.ModelSerializer):
    #文章列表
    # collected_users = serializers.StringRelatedField(read_only=True,many=True)
    # fans = serializers.StringRelatedField(read_only=True,many=True)
    collected = serializers.BooleanField(default=False)
    user = UserSerializer(read_only = True)
    class Meta:
        model = Article
        fields = ('__all__')



