from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.CharField(max_length=2, blank=True, default='')
    # def save(self, *args, **kwargs):
    #     options = {'name': self.name} if self.name else {}
    #     super(Country, self).save(*args,**kwargs)


class State(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.CharField(max_length=2, blank=True, default='')
    countryId = models.ForeignKey('Country',related_name='countries', on_delete=models.CASCADE, default='')
    def save(self, *args, **kwargs):
        options = {'name': self.name} if self.name else {}
        super(State, self).save(*args,**kwargs)

