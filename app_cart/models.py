from django.db import models
from django.conf import settings
from app_shop.models import Product
# Create your models here.

class cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name= "cart")
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'{self.quantity} x {self.item}'
    
    def get_total(self):
        total= self.item.price *self.quantity
        float_total = format(total, '0.2f')
        return float_total
    
class Order(models.Model):
    orderitems = models.ManyToManyField(cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(max_length=250, blank=True, null=True)
    orderid = models.CharField(max_length=200, blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total