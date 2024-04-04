from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('api/bookings/', views.BookingClass.as_view(),name='booking'),
    path('api/bookings/<int:pk>', views.BookingItemClass.as_view(),name='booking_item'),
]