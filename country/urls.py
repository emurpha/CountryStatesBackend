from django.conf.urls import url, include
from country import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'countries/(?P<code>\w+)/states', views.StateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]