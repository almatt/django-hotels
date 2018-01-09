from rest_framework import serializers
from dashboard.models import Hotels,City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class HotelListSerializer(serializers.ModelSerializer):
    #city = serializers.StringRelatedField(many=False)
    city = CitySerializer()
    class Meta:
        model = Hotels
        fields = '__all__'

class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

class HotelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'


class HotelDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

