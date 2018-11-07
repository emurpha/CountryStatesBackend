from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from country.models import Country, State
from rest_framework import viewsets
from country.serializers import CountrySerializer, StateSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view



class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    # def get_queryset(self):
    #     countryCode = self.kwargs.get('code')
    #     #get object or 404
    #     country=get_object_or_404(Country,code=countryCode)
    #     return country.states.all()



# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'country': reverse('country-list', request=request, format=format)
#     })