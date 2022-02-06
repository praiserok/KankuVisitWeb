from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sportsman, name='sportsman'),
    path('<int:sportsman_id>/edit',
         views.sportsmanEdit, name='sportsman-edit'),
    path('<int:sportsman_id>/delete',
         views.sportsmanDelete, name='sportsman-delete'),
]
