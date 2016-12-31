from django.conf.urls import url, include
from rest_framework import routers
from .views import APIRoot

urlpatterns = [
    url(r'^$', APIRoot.as_view(), name='root'),

    url(r'^api/', include('api_test.api.urls', namespace="api"))
]