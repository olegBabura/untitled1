from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=60)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)


class Forecast(models.Model):
    city_id = models.ForeignKey(City, null=True, blank=True)
    date = models.DateField()
    temp = models.IntegerField()
    wind_speed = models.CharField(max_length=20)
    wind_direction = models.CharField(max_length=20)
    conditions = models.CharField(max_length=60)

