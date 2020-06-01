from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Restaurant(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=50, null=False, blank=False)
    phone = PhoneNumberField()

    def __str__(self):
        return self.restaurant_name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Menu = models.CharField(max_length=50, null=False, blank=False)
    # photo = models.Image
    price = models.IntegerField()
    Info = models.TextField(max_length=500, null=False, blank=False)


