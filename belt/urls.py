from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.belt, name='belt'),
    path('<slug:slug>/edit', views.BeltEditView.as_view(), name='belt-edit'),
    path('<slug:slug>/delete', views.beltDelete, name='belt-delete'),

]
