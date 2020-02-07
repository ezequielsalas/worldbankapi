from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from core.models import Country, CountryEconomy


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name',)


class CountryEconomySerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = CountryEconomy
        fields = ('id', 'country', 'year', 'value')

    def update(self, instance, validated_data):
        country_name = validated_data.pop('country')
        for (key, value) in validated_data.items():
            setattr(instance,key,value)

        if country_name:
            country, _ = Country.objects.get_or_create(name=country_name['name'])
            instance.country = country

        instance.save()

        return instance
