import urllib2
import json
import re
import calendar
import time

from api_test.datastore import Reputation

# Known bad: 69.43.161.174
# Known good: 8.8.8.8
# Find more examples at https://www.alienvault.com/open-threat-exchange/dashboard

class IPDetails(object):
    def __init__(self, *args, **kw):
        ip = args[0]
        self.address = ip
        self.is_tracked = False
        self.is_error = False

        raw = Reputation.get_details(ip)
        
        # TODO: assign values to self
        
        return

class Reputation(object):
    @staticmethod
    def get_details(ip):
        if ip:
            try:
                # TODO: fetch raw results from the source
                # format: http://reputation.us.alienvault.com/panel/ip_json.php?ip=69.43.161.174

                url = "your-url-here" 
                return urllib2.urlopen(url).read()
            except:
                return "fetch_error"
        else:
            return None