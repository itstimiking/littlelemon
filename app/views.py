from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view

# Create your views here.



def index(request):
    return render(request, 'index.html',context={})
