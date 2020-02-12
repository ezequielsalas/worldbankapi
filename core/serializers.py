from rest_framework import serializers

from core.models import Country, CountryData, Indicator


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class IndicatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicator
        fields = ('name',)


class CountryDataSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(read_only=False,
        slug_field='name', queryset=Country.objects.all())
    indicator = serializers.SlugRelatedField(read_only=False,
        slug_field='name', queryset=Indicator.objects.all())

    class Meta:
        model = CountryData
        fields = ('id', 'country','indicator', 'year', 'value')

    def update(self, instance, validated_data):
        country_name = validated_data.pop('country', None)
        indicator_name = validated_data.pop('indicator', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if country_name:
            country, _ = Country.objects.get_or_create(name=country_name)
            instance.country = country

        if indicator_name:
            indicator, _ = Indicator.objects.get_or_create(name=indicator_name)
            instance.indicator = indicator

        instance.save()

        return instance
