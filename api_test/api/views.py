import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from api_test.datastore import IPDetails, DetailsSerializer
        
class IPDetailsView(APIView):
    def get(self, request, *args, **kw):
        try:
            [int(x) for x in args.get(ip, None).split('.')]
        except:
            return Response("invalid IP")
        
        details_request = IPDetails(ip, *args, **kw)

        result = DetailsSerializer(details_request)
        response = Response(result.data, status=status.HTTP_200_OK)

        return response

        
class Traffic(APIView):
    def get(self, request, *args, **kw):
        return Response("Feature Disabled")