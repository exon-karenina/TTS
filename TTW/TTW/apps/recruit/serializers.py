from rest_framework import serializers

from recruit.models import City, Enterprise


class CitySerializer(serializers.ModelSerializer):
    #城市序列化器
    class Meta:
        model = City
        fields = ('id','name','ishot')

class EnterpriseSerializer(serializers.ModelSerializer):
    #企业访问量
    class Meta:
        model = Enterprise
        fields = ("__all__")


