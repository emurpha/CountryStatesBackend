from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from country.models import Country, State
from rest_framework import viewsets
from country.serializers import CountrySerializer, StateSerializer, StateCreateSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view



class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    def list(self, request):
        r = super().list(self, request)
        r.data = r.data['results']
        return r

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.get_queryset()
    serializer_class = StateSerializer
    def get_queryset(self):
        countryCode = self.kwargs.get('code')
        #get object or 404
        country=get_object_or_404(Country,code=countryCode)
        return country.states.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = StateCreateSerializer
        return serializer_class

    def list(self, request, **kwargs):
        r = super().list(self, request, **kwargs)
        r.data = r.data['results']
        return r
    
    # def create(self, request, **kwargs):
    #     state = super().create(self, request, **kwargs)
    #     return state
    def post_state(self, request, **kwargs):
        state = super().create(self, request, **kwargs)
        return state

        




