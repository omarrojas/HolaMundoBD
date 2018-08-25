from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import re
# Create your views here.

@api_view(["POST"])

def IdealWeight(heightdata):
  try:
    height=json.loads(heightdata.body)
    weight=str(height*10)
    
    return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
  except ValueError as e:
    return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])

def HolaMundo(nombredata):
  try:
    nombre=json.loads(nombredata.body)
    nombrer=re.sub(r"[aeiou]","_",nombre)
    #nombrer='Omar'
    return JsonResponse("Hola "+nombrer+" !!",safe=False)
  except ValueError as e:
    return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
  
