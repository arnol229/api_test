from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from django.http import HttpResponseRedirect
import time
import requests

class APIRoot(APIView):
    def get(self, request):
        ip = request.GET.get('ip', '')
        return Response({
            'IP Details': reverse('api:threat_details', kwargs={'ip': ip}),
        })
