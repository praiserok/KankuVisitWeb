from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.SportsmanView.as_view(), name='sportsman'),
    path('<slug:slug>/edit',
         views.SportsmanEditView.as_view(), name='sportsman-edit'),
    path('<slug:slug>/delete', views.sportsmanDeleteView.as_view(),
         name='sportsman-delete'),
]
