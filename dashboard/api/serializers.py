from car.models import Car
from rest_framework import serializers
from user.models import CustomUser



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'manufacture_year']



class ProfileSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'dalal', 'cars']
