from rest_framework.views import APIView
from rest_framework import status
from rest_framework.utils import json
from rest_framework.response import Response

from core.models import CountryEconomy
from core.serializers import CountryEconomySerializer


class CountryEconomyView(APIView):
    """
       API endpoint to manage Economy by Country.
    """

    @staticmethod
    def get_object(pk):
        try:
            return CountryEconomy.objects.get(pk=pk)
        except CountryEconomy.DoesNotExist:
            return None

    def get(self, request, pk=None):
        """
        Retrieve the economy per country searching all or  by id
        """
        response = dict()
        response['status_code'] = status.HTTP_200_OK
        response['status'] = 'success'

        if pk:
            country_economy_obj = self.get_object(pk)
            if country_economy_obj:
                response['data'] = CountryEconomySerializer(country_economy_obj).data
                return Response(response)
            else:
                response['status_code'] = status.HTTP_404_NOT_FOUND
                response['status'] = 'failed'
                response['message'] = 'Data not found'
                return Response(response)

        country_economies = CountryEconomy.objects.all()
        serializer = CountryEconomySerializer(country_economies, many=True)

        if not serializer:
            response['data'] = []
            return Response(response)

        response['data'] = serializer.data

        return Response(response)

    def patch(self, request, pk=None):
        """
        Update the economy per country partially
        """
        response = {}
        country_economy = json.loads(request.body.decode('utf-8'))

        country_economy_obj = self.get_object(pk)
        if country_economy_obj is None:
            response['status_code'] = status.HTTP_404_NOT_FOUND
            response['status'] = 'failed'
            response['message'] = 'Country economy not found'
            return Response(response)

        serializer = CountryEconomySerializer(country_economy_obj, data=country_economy, partial=True)
        if serializer.is_valid(raise_exception=True):
            country_economy_saved = serializer.save()
            response['status_code'] = status.HTTP_201_CREATED
            response['status'] = 'success'
            response['message'] = 'The data was updated successfully'
            response['data'] = {'countryEconomies': CountryEconomySerializer(country_economy_saved).data}

        return Response(response)
