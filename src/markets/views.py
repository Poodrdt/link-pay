from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsThisMarketManager
from .models import *
from .serializers import *


class ShopLinksView(TemplateView):
    template_name = "markets/test.html"

    def get_context_data(self, **kwargs):
        print(self.request.user)
        print(bool(self.request.user.groups.filter(name="MarketManager").first()))


class ShopViewSet(viewsets.ModelViewSet):
    permission_classes = (IsThisMarketManager,)
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def retrieve(self, request, pk=None):
        obj = self.get_object()
        self.check_object_permissions(self.request, obj)
        res = super().retrieve(request, pk)
        return res


class MarketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class ClickCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CallbackSerializer
    queryset = Click.objects.all()


class CallbackCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CallbackSerializer
    queryset = Callback.objects.all()


class MarketStatisticsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                                      viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)                                                  
    serializer_class = MarketStatisticsSerializer
    queryset = Market.objects.filter(active=True)


class ShopStatisticsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                                    viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)                                                   
    serializer_class = ShopStatisticsSerializer
    queryset = Shop.objects.filter(active=True)
