from rest_framework import serializers
from .models import *


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'link', 'price', 'active', 'markets')

    def to_representation(self, obj):
        ret = super(ShopSerializer, self).to_representation(obj)
        if not obj.active:
            ret['link'] = ['Shop is not avaliable']
        return ret 


class MarketSerializer(serializers.ModelSerializer):
    
    shops = ShopSerializer(many=True, required=False)

    class Meta:
        model = Market
        fields = ('id', 'name', 'alias', 'shops', 'active')

    def to_representation(self, obj):
        ret = super(MarketSerializer, self).to_representation(obj)
        if not obj.active:
            ret['shops'] = [{'message': 'Market is not active'}]
        return ret 


class CallbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Callback
        fields = ('time', 'shop')


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Click
        fields = ('time', 'shop')


class ShopStatisticsSerializer(serializers.ModelSerializer):

    callbacks = serializers.CharField(source='get_shop_callbacks')
    clicks = serializers.CharField(source='get_shop_clicks')
    shop_sum = serializers.CharField(source='get_shop_sum')

    class Meta:
        model = Shop
        fields = ('name', 'callbacks', 'clicks', 'shop_sum')


class MarketStatisticsSerializer(serializers.ModelSerializer):

    callbacks = serializers.CharField(source='get_market_shops_callbacks')
    clicks = serializers.CharField(source='get_market_shops_clicks')
    market_sum = serializers.CharField(source='get_market_sum')
    shops = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='shop-statistics-detail'
    )

    class Meta:
        model = Market
        fields = ('name', 'shops', 'callbacks', 'clicks', 'market_sum')