from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.PositiveIntegerField()
    # product_date = models.DateField(null=True, auto_created=True)

    def __str__(self):
        return f"{self.title} - {self.price}"


    def get_absolute_url(self):
        return reverse("product_detail", args=(self.slug, ))
