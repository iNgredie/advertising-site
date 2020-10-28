from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photos_urls = models.CharField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)


