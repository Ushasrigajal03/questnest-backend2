# backend2/api/views.py
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "healthy", "service": "backend2"}, status=status.HTTP_200_OK)

class ServiceInfoView(APIView):
    def get(self, request):
        return Response({
            "service": "backend2",
            "data": {
                "name": "Backend Service 2",
                "version": "1.0.0",
                "features": ["data-processing", "analytics", "reporting"]
            }
        })

class Backend1ProxyView(APIView):
    """View to demonstrate backend-to-backend communication"""
    def get(self, request):
        try:
            # Assuming backend1 is accessible via Traefik at this URL
            backend1_url = 'http://backend1.questnest.in/api/users/'
            
            # Forward the request to backend1 with proper API key
            response = requests.get(
                backend1_url,
                headers={settings.API_KEY_HEADER: 'backend1-secret-key'},
                timeout=5
            )
            
            # Return the data from backend1 along with metadata
            return Response({
                "service": "backend2",
                "proxied_response": response.json(),
                "status": "success"
            })
        except Exception as e:
            return Response({
                "service": "backend2",
                "error": str(e),
                "status": "failed"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)