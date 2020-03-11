from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, UpdateAPIView, GenericAPIView
from rest_framework.response import Response

from recruit.models import City, Enterprise
from recruit.serializers import CitySerializer, EnterpriseSerializer


class CityView(ListAPIView):
    #热门城市
    queryset = City.objects.filter(ishot = 1)
    serializer_class = CitySerializer

class EnterpriseView(GenericAPIView):
    #修改企业访问次数
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    def put(self, request, pk):
        recruit = self.get_object()
        recruit.visits += 1
        recruit.save()
        return Response({'success': True, 'message': '更新成功'})
