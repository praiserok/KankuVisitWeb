from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.school, name='school'),
    path('<int:pk>/edit', views.SchoolEditView.as_view(), name='school-edit'),
    path('<int:pk>/delete', views.schoolDelete, name='school-delete'),
]
