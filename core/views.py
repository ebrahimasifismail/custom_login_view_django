from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def base(request):
    return HttpResponse("Welcome to Webapp. Be happy.. your are the first one here!")