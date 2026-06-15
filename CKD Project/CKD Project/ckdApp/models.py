from django.db import models

# Create your models here.
class ckdModel(models.Model):

    Area=models.FloatField()
    Bedrooms=models.FloatField()
    Bathrooms=models.FloatField()
    Floors=models.FloatField()
    YearBuilt=models.FloatField()
    Location=models.FloatField()
    Condition=models.FloatField()
    Garage=models.FloatField()
    Location_ratio=models.FloatField()
