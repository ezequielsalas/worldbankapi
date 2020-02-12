from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.utils import json
from rest_framework.response import Response

from core.models import CountryData, Country, Indicator
from core.serializers import CountryDataSerializer


class CountryDataView(APIView):
    """
       API endpoint to manage Data by Country.
    """

    @staticmethod
    def get_object(pk):
        try:
            return CountryData.objects.get(pk=pk)
        except CountryData.DoesNotExist:
            return None

    def get(self, request, pk=None):
        """
        Retrieve the data per country searching all or  by id
        """
        response = dict()
        response['status_code'] = status.HTTP_200_OK
        response['status'] = 'success'

        if pk:
            country_data_obj = self.get_object(pk)
            if country_data_obj:
                response['data'] = CountryDataSerializer(country_data_obj).data
                return Response(response)
            else:
                response['status_code'] = status.HTTP_404_NOT_FOUND
                response['status'] = 'failed'
                response['data'] = []
                response['message'] = 'Data not found'
                return Response(response)

        country_data = CountryData.objects.all()
        serializer = CountryDataSerializer(country_data, many=True)

        if not serializer:
            response['data'] = []
            return Response(response)

        response['data'] = serializer.data

        return Response(response)

    def patch(self, request, pk=None):
        """
        Update the data per country partially
        """
        response = {}
        country_data = json.loads(request.body.decode('utf-8'))

        country_data_obj = self.get_object(pk)
        if country_data_obj is None:
            response['status_code'] = status.HTTP_404_NOT_FOUND
            response['status'] = 'failed'
            response['data'] = []
            response['message'] = 'Country Data not found'
            return Response(response)

        serializer = CountryDataSerializer(country_data_obj, data=country_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            country_data_saved = serializer.save()
            response['status_code'] = status.HTTP_201_CREATED
            response['status'] = 'success'
            response['message'] = 'The data was updated successfully'
            response['data'] = {'countryData': CountryDataSerializer(country_data_saved).data}

        return Response(response)


def load_dropdown(request):
    """
    This endpoint is used to fill the dropdown in the table
    """
    countries = Country.get_list_name()
    indicators = Indicator.get_list_name()
    return JsonResponse({"countries": countries, "indicators":indicators})
