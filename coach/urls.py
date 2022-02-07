from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.coach, name='coach'),
    path('<int:pk>/edit',
         views.CoachEditView.as_view(), name='coach-edit'),
    path('<int:pk>/delete',
         views.coachDelete, name='coach-delete'),
]
