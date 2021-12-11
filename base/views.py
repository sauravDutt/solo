from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(requenst):
    return render(requenst, 'base/home.html')

