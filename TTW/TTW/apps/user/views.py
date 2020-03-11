from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from user.models import User


from user.serializers import UserCreateSerializer, UserPasswordSerializer


#创建用户
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


#修改密码
class UserPasswordView(UpdateAPIView):
    serializer_class = UserPasswordSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
