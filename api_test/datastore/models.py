# from django.db import models
# from django.utils.dateformat import format
# from django.utils.crypto import get_random_string

# class User(models.Model):
#     """
#     Base User model
#     """
#     alienvault_id = models.CharField(max_length=12, primary_key=True)

#     class META:
#         app_label = 'datastore'

#     @staticmethod
#     def create_with_id():
#         AvID = str(get_random_string(length=12))
#         return User.objects.create(alienvault_id=AvID)

#     def get_visits(self):
#         return {
#             "alienvaultid": self.alienvault_id,
#             "visits": [visit.to_json() for visit in Visit.objects.filter(user=self)]
#         }


# class Visit(models.Model):
#     """
#     Database Record of a users api activity.
#     """
#     user = models.ForeignKey(User)
#     address = models.CharField(max_length=12)
#     created = models.DateTimeField(auto_now_add=True)
#     endpoint = models.CharField(max_length=12)
#     result = models.BooleanField()

#     def to_json(self):
#         return {
#             "address": self.address,
#             "timestamp": format(self.created, 'U'),
#             "endpoint": self.endpoint
#         }
