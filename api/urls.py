# backend2/api/urls.py
from django.urls import path
from .views import HealthCheckView, ServiceInfoView, Backend1ProxyView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health'),
    path('info/', ServiceInfoView.as_view(), name='info'),
    path('call-backend1/', Backend1ProxyView.as_view(), name='call-backend1'),
]