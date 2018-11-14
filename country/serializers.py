from country.models import Country, State
from rest_framework import serializers
from django.shortcuts import get_object_or_404


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'code', 'name', 'countryId')

class StateCreateSerializer(serializers.ModelSerializer):

    country_code = serializers.CharField(source='countryId.code')

    class Meta:
        model = State
        fields = ['code','name','country_code']

    def create(self, validated_data):
        print ('\n\n\n\n\nValidated_Data:' + str(validated_data) + '\n\n\n\n\n')
        country_object = validated_data.pop('countryId')
        country = country_object.pop('code')
        country = get_object_or_404(Country, code=country)
        # state = State.objects.create(**validated_data, countryId=country)
        state = State.objects.create(
            code = validated_data['code'],
            name = validated_data['name'],
            countryId = country,
        )
        return state
        return state