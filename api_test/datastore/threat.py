from api_test.datastore import DetailsSerializer
from django.conf import settings
import requests

class IPDetails(object):
    def __init__(self, *args, **kw):
        self.address = kw.get('address')
        # self.is_tracked = kw.get('is_tracked')
        # self.is_error = False

        # IP Detail fields
        self.id = kw.get('id', '')
        self.reputation_val = kw.get('reputation_val', 0)
        self.first_activity = kw.get('first_activity', None)
        self.last_activity = kw.get('last_activity', None)
        self.activities = kw.get('activities', [])
        self.activity_types = kw.get('activity_types', [])
        self.is_valid = kw.get('is_valid', False)

    @staticmethod
    def get_details(ip):
        """
        Retrieves ip details and validates data against the DetailsSerializer
        If valid, creates and returns an IPDetails object 
        """
        try:
            url = settings.ROUTES['IPDetails']
            result = requests.get(url, params={'ip':ip})
            if not result.text:
                return IPDetails({"address": ip})

            mapped_results = DetailsSerializer.map_details(result.json())
            serializer = DetailsSerializer(data=mapped_results)

            if serializer.is_valid():
                ip_details = serializer.validated_data.copy()
                ip_details.update({'is_valid': True})
                return IPDetails(**ip_details)
            else:
                ip_details = {"address": ip}

            return IPDetails(ip_details)
        except Exception as e:
            raise Exception("IP details error: {0}".format(str(e)))

    def to_json(self):
        return {
            "is_valid": self.is_valid,
            "address": self.address,
            "id": self.id,
            "Reputation_val": self.reputation_val,
            "first_activity": self.first_activity,
            "Last_activity": self.last_activity,
            "Activity_types": self.activity_types
        }
