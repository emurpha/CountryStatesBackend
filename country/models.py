from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.CharField(max_length=2, blank=True, default='')



class State(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.CharField(max_length=2, blank=True, default='')
    countryId = models.ForeignKey('Country', on_delete=models.CASCADE)

