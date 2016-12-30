from django.conf.urls import url, include
from rest_framework import routers
from server import APIRoot

urlpatterns = [
    url(r'^$', APIRoot.as_view(), name='root'),

    url(r'^api/', include('api.urls', namespace="api"))
]