from rest_framework import serializers
from .models import Service
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.settings import api_settings


from .models import Service

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'text','picture')


class jwtserializer(serializers.ModelSerializer):
    UserModel = get_user_model()
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    class Meta:
        model = Service
        fields = '__all__'