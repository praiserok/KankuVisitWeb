from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexVisit, name='visit'),
    path('coach/', include('coach.urls')),
    path('sportsman/', include('sportsman.urls')),
    path('school/', include('school.urls')),
    path('belt/', include('belt.urls')),


    path('about', views.about, name='about'),



]
