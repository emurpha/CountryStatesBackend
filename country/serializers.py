from country.models import Country, State
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name')

class StateSerializer(serializers.ModelSerializer):
    # countryCode = 
    class Meta:
        model = State
        fields = ('id', 'code', 'name', 'countryId')

