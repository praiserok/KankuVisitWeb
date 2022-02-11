from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sportsman, name='sportsman'),
    path('<slug:slug>/edit',
         views.SportsmanEditView.as_view(), name='sportsman-edit'),
    path('<slug:slug>/delete',
         views.sportsmanDelete, name='sportsman-delete'),
]
