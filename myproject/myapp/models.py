from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class category(models.Model):
    categoryname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoryname


class item(models.Model):
    itemname = models.CharField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=255)
    photo1 = models.ImageField(upload_to='item/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='item/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='item/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='item/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Cart(models.Model):
    usr = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(item, on_delete=models.CASCADE)
    color = models.CharField(max_length=255,null=True, blank=True)
    size = models.CharField(max_length=255,null=True, blank=True)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Cart : "+ str(self.cart.id)+ "CartProduct : " + str(self.id)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=255,null=True, blank=True)
    shipping_address = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255,null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)