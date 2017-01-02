from rest_framework import serializers

from operator import getitem
def dot_get(data, s, default=None):
    """
    helper function to drill into multilayer JSON object cleanly.
    akin to Javascript's lodash/underscore .get function
    """
    try:
        return reduce(getitem, s.split('.'), data)
    except KeyError:
        return default

class DetailsSerializer(serializers.Serializer):
    address = serializers.Field()
    id = serializers.Field()
    reputation_val = serializers.Field()
    first_activity = serializers.Field()
    last_activity = serializers.Field()
    activities = serializers.Field()
    activity_types = serializers.Field()
    is_valid = serializers.Field()

    def to_internal_value(self, data):
        return data

    @staticmethod
    def map_details(data):
        try:
            activities = [{
                "Activity_type": a.get("name", None),
                "First_date": dot_get(a, 'first_date.sec'),
                "Last_date": dot_get(a, 'last_date.sec'),
                    } for a in data.get("activities", [])]

            timestamped_activities = filter(lambda k: k.get("Last_date") is not None, activities)
            first_activity_time = min([a['First_date'] for a in timestamped_activities])
            last_activity_time = max([a['Last_date'] for a in timestamped_activities])
            activity_types = list(set([a['Activity_type'] for a in activities]))

            return {
                "address": data.get("address"),
                "id": dot_get(data, "_id.$id"),
                "last_activity": last_activity_time,
                "first_activity": first_activity_time,
                "reputation_val": data.get("reputation_val", None),
                "activities": activities,
                "activity_types": activity_types
            }
        except Exception as e:
            return {}
