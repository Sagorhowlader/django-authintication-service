from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User



# Create your views here.

class Registration(APIView):
    def post(self, request):
        return Response({'status': 200})
