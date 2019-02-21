from django.db import models


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
        return self.name

    def create_link(self):
        return {'name': self.name}

    def get_links(self):
        return self.objects.filter()



class Market(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, unique=True)
    shops = models.ManyToManyField(Shop)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_market_shops_callbacks(self):
        return Callback.objects.filter(shop__market_shops__market=self, active=True)


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

