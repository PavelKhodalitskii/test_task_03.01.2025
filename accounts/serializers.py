from django.contrib.auth.models import User
from rest_framework import serializers


class UserTruncDataSerializer(serializers.ModelSerializer):
    '''
    Сериалиазтор модели пользователя с минимальными данными
    '''
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']
        read_only_fields = ["first_name", "last_name",]