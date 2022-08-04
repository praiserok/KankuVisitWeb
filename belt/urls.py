from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.BeltView.as_view(), name='belt'),
    path('<slug:slug>/edit', views.BeltEditView.as_view(), name='belt-edit'),
    path('<slug:slug>/delete', views.beltDeleteView.as_view(), name='belt-delete'),

]
