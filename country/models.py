from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    code = models.CharField(max_length=2, blank=False, default='')



class State(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    code = models.CharField(max_length=2, blank=False, default='')
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='states')

