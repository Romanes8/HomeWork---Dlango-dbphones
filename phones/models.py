from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    price = models.FloatField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length=50, null=True, unique=True)




