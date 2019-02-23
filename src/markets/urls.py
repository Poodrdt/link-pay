from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'market', MarketViewSet, base_name='market')
router.register(r'shop', ShopViewSet, base_name='shop')
router.register(r'callback', CallbackCreateViewSet, base_name='callback')
router.register(r'click', ClickCreateViewSet, base_name='click')
router.register(r'market-statistics', MarketStatisticsViewSet, base_name='market-statistics')
router.register(r'shop-statistics', ShopStatisticsViewSet, base_name='shop-statistics')


urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('', ShopLinksView.as_view(), name='shop-links'),
]
