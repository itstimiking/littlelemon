from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics 
from . import models
from . import serializers

# Create your views here.



def index(request):
    return render(request, 'index.html',context={})

class BookingClass(generics.ListCreateAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    
class BookingItemClass(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

