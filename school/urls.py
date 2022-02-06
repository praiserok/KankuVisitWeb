from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.school, name='school'),
    path('<int:school_id>/edit', views.schoolEdit, name='school-edit'),
    path('<int:school_id>/delete', views.schoolDelete, name='school-delete'),
]
