from django.urls import path

from .views import CountryEconomyView

urlpatterns = [
    path('display_data/', CountryEconomyView.as_view(), None, "country_economy"),
    path('display_data/<int:pk>', CountryEconomyView.as_view(), None, "country_economy"),
]