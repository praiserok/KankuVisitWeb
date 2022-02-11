from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.school, name='school'),
    path('<slug:slug>/edit', views.SchoolEditView.as_view(), name='school-edit'),
    path('<slug:slug>/delete', views.schoolDelete, name='school-delete'),
]
