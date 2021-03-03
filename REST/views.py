
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.

global data;
data = ['test']

class PersonView(APIView):
    def get(self, request, format=None):
        message = {
            'Response':200,
            'Message' : 'Welcome to django rest API'

        }
        return Response(message)

    def post(self, request, format=None):
        datam = request.data
        name = datam.get('name', None)
        data.append(name)
        message = {
            'Response': 200,
            'Message': 'Welcome to django rest API',
            'data': data
        }
        return Response(message)


from .serializer import DummySerializer
class WeatherViews(generics.CreateAPIView):
    serializer_class = DummySerializer
    def create(self, request, *args, **kwargs):
        try:
            zip = request.data.get('zip')
            city = request.data.get('city')
            age = request.data.get('age')
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "message" : "Failed"
            })
