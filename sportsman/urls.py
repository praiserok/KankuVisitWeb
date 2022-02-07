from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sportsman, name='sportsman'),
    path('<int:pk>/edit',
         views.SportsmanEditView.as_view(), name='sportsman-edit'),
    path('<int:pk>/delete',
         views.sportsmanDelete, name='sportsman-delete'),
]
