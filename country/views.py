from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from country.models import Country, State
from rest_framework import viewsets
from country.serializers import CountrySerializer, StateSerializer, StateCreateSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view



class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer
    def list(self, request):
        r = super().list(self, request)
        r.data = r.data['results']
        return r

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.get_queryset()
    def get_queryset(self):
        countryCode = self.kwargs.get('code')
        country=get_object_or_404(Country,code=countryCode)
        return country.states.all().order_by('name')
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = StateCreateSerializer
        else:
            serializer_class = StateSerializer
        return serializer_class

    def list(self, request, **kwargs):
        r = super().list(self, request, **kwargs)
        r.data = r.data['results']
        return r
    


        




