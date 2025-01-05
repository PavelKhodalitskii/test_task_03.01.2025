from rest_framework import serializers
from django.contrib.auth.models import User

from cars_manager.models import Car, Brand, Comments
from accounts.serializers import UserTruncDataSerializer


class BrandSerializer(serializers.ModelSerializer):
    '''
    Базовый сериализатор модели "Brand" 
    '''
    class Meta:
        model = Brand
        fields = "__all__"

class CommentsBaseSerializer(serializers.ModelSerializer):
    '''
    Базовый сериализатор модели "Comment" 
    '''
    class Meta:
        model = Comments
        fields = "__all__"

class CarBaseSerializer(serializers.ModelSerializer):
    '''
    Базовый сериализатор модели "Car" 
    '''
    make = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Car
        fields = "__all__"

class CarDetailSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели "Car" с подробной информацией о 
    производителе ("make")
    и 
    владельце ("owner")
    '''
    make = BrandSerializer()
    owner = UserTruncDataSerializer()

    class Meta:
        model = Car
        fields = "__all__"