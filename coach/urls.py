from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.coach, name='coach'),
    path('<int:coach_id>/edit',
         views.coachEdit, name='coach-edit'),
    path('<int:coach_id>/delete',
         views.coachDelete, name='coach-delete'),
]
