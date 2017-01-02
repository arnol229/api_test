import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from django.utils.decorators import method_decorator
from api_test.decorators import api_response

from api_test.datastore import IPDetails, DetailsSerializer
from .models import User


class IPDetailsView(APIView):
    @method_decorator(api_response)
    def dispatch(self, *args, **kwargs):
        return super(IPDetailsView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kw):
        # look for ip from request path, if not then try GET param
        ip = kw.get("ip", request.GET.get("ip", None))
        try:
            [int(x) for x in ip.split('.')]
        except:
            return Response("invalid IP")
        details_request = IPDetails.get_details(ip)

        result = DetailsSerializer(details_request)
        response = Response(result.data, status=status.HTTP_200_OK)

        return response


class Traffic(APIView):
    def get(self, request, *args, **kw):
        # if not request.GET.get("super_secret_admin_mode"):
        #     traffic_data = request.user.get_visits()
        # else:
        traffic_data = [u.get_visits() for u in User.objects.all()]
        return Response(traffic_data)
