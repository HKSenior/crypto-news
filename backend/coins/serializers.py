from rest_framework import serializers

from .models import Coin


class CoinSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Coin.objects.create(**validated_data)

    class Meta:
        model = Coin
        fields = '__all__'
