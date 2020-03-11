import re

from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """创建用户的序列化器"""
    sms_code = serializers.CharField(label='短信验证码', write_only=True)
    token = serializers.CharField(label='JWT token', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'sms_code', 'mobile', 'token','avatar')
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

    def validate(self, data):
        mobile = data['mobile']
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            raise serializers.ValidationError('手机号格式错误')
        redis_conn = get_redis_connection('verify_code')
        real_sms_code = redis_conn.get('sms_%s' % mobile)
        if real_sms_code is None:
            raise serializers.ValidationError('无效的短信验证码')
        if data['sms_code'] != real_sms_code.decode():
            raise serializers.ValidationError('短信验证码错误')

        return data
    def create(self, validated_data):
        del validated_data['sms_code']
        user =super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # 签发jwt token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        user.token = token

        return user


class UserPasswordSerializer(serializers.ModelSerializer):
    """
        用户详修改密码序列化器
        """

    class Meta:
        model = User
        fields = ('password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        user = super.update(isinstance,validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user