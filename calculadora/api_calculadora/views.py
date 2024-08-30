import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Create your views here.
class SumaView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        suma =int(num_uno) + int(num_dos)
        return  Response(suma, status=status.HTTP_200_OK)
    
class RestaView(APIView):

    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        suma =int(num_uno) - int(num_dos)
        return  Response(suma, status=status.HTTP_200_OK)
    
class MultiplicacionView(APIView):

    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        suma =int(num_uno) * int(num_dos)
        return  Response(suma, status=status.HTTP_200_OK)
    
class DivisionView(APIView):

    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        
        if int(num_dos) == 0:
            return Response("error: División por cero no permitida.", status=status.HTTP_400_BAD_REQUEST)
        
        suma =int(num_uno)/ int(num_dos)
        return  Response(suma, status=status.HTTP_200_OK)
    


    

