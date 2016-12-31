import requests
from django.conf import settings

class Reputation(object):
    @staticmethod
    def get_details(ip):
        if ip:
            try:
                url = settings.ROUTES['IPDetails']
                return requests.get(url, params={'ip':ip}).json()
            except:
                return "fetch_error"
        else:
            return None