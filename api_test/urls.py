from django.conf.urls import url, include
from .views import APIRoot

from .decorators import api_response

urlpatterns = [
    url(r'^$', APIRoot.as_view(), name='root'),
    url(r'^api/', include('api_test.api.urls', namespace="api"))
]
