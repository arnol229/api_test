from django.conf.urls import url, include
from rest_framework import routers
import views

urlpatterns = [
    url(r'^$', views.APIRoot.as_view(), name='api_root'),
    
    # TODO: match /api/threat/ip/1.2.3.4
    url(r'<your regex here>', ip_views.IPDetailsView.as_view(), name='threat_details'),
    
    # TODO: match /api/traffic
]