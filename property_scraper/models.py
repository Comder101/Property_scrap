from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    link = models.URLField(max_length=500)

class CronJobSettings(models.Model):
    enabled = models.BooleanField(default=True)

class ScrapingLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    records_scraped = models.PositiveIntegerField()