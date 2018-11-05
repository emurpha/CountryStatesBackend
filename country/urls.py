from django.conf.urls import url, include
from country import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'countries/<countrycode>/states', views.StateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]