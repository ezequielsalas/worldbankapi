from django.urls import path

from .views import CountryDataView, load_dropdown

urlpatterns = [
    path('display_data/', CountryDataView.as_view(), None, "display_data"),
    path('display_data/<int:pk>/', CountryDataView.as_view(), None, "display_data"),
    path('load_dropdown/', load_dropdown, None, "load_dropdown"),
]