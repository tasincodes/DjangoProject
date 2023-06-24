from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect

from first.models import *
from django.views import View

# Create your views here.

def home(request):
    return HttpResponse("helllo tasin")