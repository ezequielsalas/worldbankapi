from django.contrib import admin

from core.models import Country, CountryData, Indicator

admin.site.register(Country)
admin.site.register(Indicator)
admin.site.register(CountryData)
