from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from colorfield.fields import ColorField

class Integration(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    photo = models.ImageField()


class Template(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField()
    link = models.URLField(max_length=100)

class Order(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField()
    description = models.CharField(max_length=500)
    template = models.ImageField()
    integrations = models.ManyToManyField(Integration)
    sum_to_pay = models.DecimalField(max_digits=11, decimal_places=2)
    email = models.EmailField(max_length=254)
    template_type = models.CharField(max_length=100)
    template_comments = models.CharField(max_length=500)
    file = models.FileField(upload_to=None, max_length=100)
    other_comments = models.CharField(max_length=500)

class Color(models.Model):
    addcolor = ColorField(null=True, blank=True)

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    status = models.CharField(max_length=40)

class Setting(models.Model):
    price_template_shop = models.DecimalField(max_digits=11, decimal_places=2)
    price_template_shop_adjustment = models.DecimalField(max_digits=11, decimal_places=2)
    price_template_wrapbootstrap = models.DecimalField(max_digits=11, decimal_places=2)
    price_custom_template = models.DecimalField(max_digits=11, decimal_places=2)
    contact_email = models.EmailField(max_length=254)
    contact_phone = PhoneNumberField(null=False, blank=False, unique=True)
    key_for_paying = models.IntegerField(primary_key=True)

# Create your models here.
