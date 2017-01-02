from django.conf.urls import url, patterns
from .views import IPDetailsView, Traffic


urlpatterns = patterns('api_test.api.views',
    url(r'threat/ip/(?P<ip>.*)$', IPDetailsView.as_view(), name='threat_details'),
    url(r'traffic$', Traffic.as_view(), name='traffic')
)
