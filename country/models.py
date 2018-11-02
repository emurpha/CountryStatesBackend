from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200)

class State(models.Model):
    state_name = models.CharField(max_length=200)
    state_code = models.CharField(max_length=200)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

