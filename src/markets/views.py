from django.views.generic import TemplateView
from rest_framework import viewsets, generics, mixins
from rest_framework import IsAuthentificated
from .permissions import IsThisMarketManager
from .models import *
from .serializers import *


class ShopLinksView(TemplateView):
    pass

class ShopViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthentificated,)
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class MarketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsThisMarketManager,)

    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class ClickCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CallbackSerializer
    queryset = Click.objects.all()


class CallbackCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CallbackSerializer
    queryset = Callback.objects.all()

