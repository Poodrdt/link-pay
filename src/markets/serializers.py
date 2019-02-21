from rest_framework import serializers
from .models import *


class MarketSerializer(serializers.ModelSerializer):
    # permission_classes = (IsAuthenticated,)
    shops = serializers.StringRelatedField(many=True)

    class Meta:
        model = Market
        fields = ('id', 'name', 'alias', 'shops', 'active')


class ShopSerializer(serializers.ModelSerializer):
    # permission_classes = (IsAuthenticated,)

    markets = MarketSerializer(many=True, required=False)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'link', 'price', 'active', 'markets')

    def to_representation(self, obj):
        ret = super(ShopSerializer, self).to_representation(obj)
        if not obj.active:
            print(ret)
            ret['link'] = 'Shop is not avaliable'
        return ret 


class CallbackSerializer(serializers.ModelSerializer):
    # shop = serializers.RelatedField(queryset=Shop.objects.all())

    class Meta:
        model = Callback
        fields = ('time', 'shop')


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Click
        fields = ('time', 'shop')
