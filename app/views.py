from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
# Create your views here.

def home(request):

    return render(request, 'index.html')