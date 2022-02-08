from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.belt, name='belt'),
    path('<int:pk>/edit', views.BeltEditView.as_view(), name='belt-edit'),
    path('<int:pk>/delete', views.beltDelete, name='belt-delete'),

]
