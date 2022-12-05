from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        abstract = True


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    objects = models.Manager()
    tags = TaggableManager(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['brand', 'name'],
                name="unique_product_with_a_particular_brand")
        ]

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class PurchasedProduct(TimestampedModel):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    opened = models.DateField(blank=True, null=True)
    finished = models.DateField(blank=True, null=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} bought in {self.shop.name}'
