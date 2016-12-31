from api_test.datastore import Reputation

class IPDetails(object):
    def __init__(self, *args, **kw):
        ip = args[0]
        self.address = ip
        self.is_tracked = False
        self.is_error = False

        raw = Reputation.get_details(ip)
        
        # TODO: assign values to self
        
        return