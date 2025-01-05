from rest_framework import serializers
from django.contrib.auth.models import User

from cars_manager.models import Car, Brand
from accounts.serializers import UserTruncDataSerializer


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class CarBaseSerializer(serializers.ModelSerializer):
    make = BrandSerializer(many=False)
    owner = UserTruncDataSerializer(many=False)

    class Meta:
        model = Car
        fields = "__all__"