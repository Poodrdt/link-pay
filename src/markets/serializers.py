from rest_framework import serializers
from .models import *


class ShopSerializer(serializers.ModelSerializer):
    # permission_classes = (IsAuthenticated,)
    class Meta:
        model = Shop
        fields = ('id', 'name', 'link', 'price', 'active')


class MarketSerializer(serializers.ModelSerializer):
    # permission_classes = (IsAuthenticated,)
    shops = serializers.RelatedField(queryset=Shop.objects.all(), many=True)

    class Meta:
        model = Market
        fields = ('id', 'name', 'alias', 'shops', 'active')



class CallbackSerializer(serializers.ModelSerializer):
    # shop = serializers.RelatedField(queryset=Shop.objects.all())

    class Meta:
        model = Callback
        fields = ('time', 'shop')

    # def create(self, validated_data):
    #     shop = validated_data.pop('shop')
    #     shop_instance, created = Tag.objects.get_or_create(name=shop)
    #     article_instance = Shop.objects.create(**validated_data, shop=shop_instance)
    #     return article_instance


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Click
        fields = ('time', 'shop')