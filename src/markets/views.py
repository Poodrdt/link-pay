from django.views.generic import TemplateView
from rest_framework import viewsets, generics, mixins
from .models import *
from .serializers import *


class ShopLinksView(TemplateView):
    pass

class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todo Lists to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class MarketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todo Lists Entrys to be viewed or edited.
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class ClickCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CallbackSerializer
    queryset = Click.objects.all()


class CallbackCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CallbackSerializer
    queryset = Callback.objects.all()

