from django.urls import path

from .views import CountryDataView

urlpatterns = [
    path('display_data/', CountryDataView.as_view(), None, "display_data"),
    path('display_data/<int:pk>', CountryDataView.as_view(), None, "display_data"),
]