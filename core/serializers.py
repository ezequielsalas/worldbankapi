from rest_framework import serializers

from core.models import Country, CountryData, Indicator


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name',)


class IndicatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicator
        fields = ('id','name','code')


class CountryDataSerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()
    indicator = IndicatorSerializer()

    class Meta:
        model = CountryData
        fields = ('id', 'country','indicator', 'year', 'value')

    def update(self, instance, validated_data):
        country_name = validated_data.pop('country', None)
        indicator_code = validated_data.pop('indicator', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if country_name:
            country, _ = Country.objects.get_or_create(name=country_name['name'])
            instance.country = country

        if indicator_code:
            indicator, _ = Indicator.objects.get_or_create(code=indicator_code['code'])
            instance.indicator = indicator

        instance.save()

        return instance
