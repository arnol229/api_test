from rest_framework import serializers
from threat import IPDetails

class DetailsSerializer(serializers.Serializer):
    is_valid = serializers.Field()
    address = serializers.Field()
    is_tracked = serializers.Field()

    # TODO: serialize the rest of your values in IPDetails here
    # use of the simple serializers.Field() is acceptable