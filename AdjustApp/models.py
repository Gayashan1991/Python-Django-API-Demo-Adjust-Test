from django.db import models

# Create your models here.
class Metric(models.Model):
    date = models.CharField(max_length=12)
    channel = models.CharField(max_length=100)
    country = models.CharField(max_length=4)
    os = models.CharField(max_length=20)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

