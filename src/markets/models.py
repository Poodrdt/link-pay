from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Shop(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(
        max_length=128, 
        # db_index=True, 
        unique=True, 
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        link = self.link if self.active else "Inactive"
        return self.name

    def get_shop_callbacks(self):
        return Callback.objects.filter(shop=self).count()

    def get_shop_clicks(self):
        return Click.objects.filter(shop=self).count()

    def get_shop_sum(self):
        res =  Callback.objects.filter(shop=self).aggregate(models.Sum('shop__price'))
        return res['shop__price__sum']


class Market(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, unique=True)
    shops = models.ManyToManyField(Shop, related_name='markets')
    managers = models.ManyToManyField(User, related_name='markets')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_market_shops_callbacks(self):
        return Callback.objects.filter(shop__markets=self).count()

    def get_market_shops_clicks(self):
        return Click.objects.filter(shop__markets=self).count()

    def get_market_sum(self):
        res = Callback.objects.filter(
            shop__markets=self,
            shop__active=True
        ).aggregate(models.Sum('shop__price'))
        return res['shop__price__sum']


class Click(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shop} {self.time}"


class Callback(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shop} {self.time}"
