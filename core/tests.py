from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from core.models import Country, Indicator, CountryData
from core.serializers import CountryDataSerializer
from rest_framework.views import status


class CountryDataTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        country_1 = Country.objects.create(name="USA")
        country_2 = Country.objects.create(name="Dominican Republic")

        indicator_1 = Indicator.objects.create(name="Indicator 001", code="Code 001")
        indicator_2 = Indicator.objects.create(name="Indicator 002", code="Code 002")

        CountryData.objects.create(country=country_1, indicator=indicator_1, year=2001, value=1000.39)
        CountryData.objects.create(country=country_2, indicator=indicator_2, year=2002, value=2000.40)

    def test_get_all_country_data(self):
        """
            This test ensures that all countryData added in the setUp method
            exist when we make a GET request to the display_data/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("display_data")
        )

        expected = CountryData.objects.all()
        serialized = CountryDataSerializer(expected, many=True)
        self.assertEqual(response.data['data'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_country_data(self):
        """
            This test ensures that a countryData is updated when we make a PATCH request to the display_data/:pk endpoint
        """
        expected = CountryData.objects.get(indicator__code="Code 001", year=2001, country__name="USA")
        expected.year = 2020

        # hit the API endpoint
        response = self.client.patch(reverse("display_data", None, [expected.pk]), {
            "year": expected.year
        }, format='json')

        serialized = CountryDataSerializer(expected, many=False)
        self.assertEqual(response.data['data']['countryData'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
