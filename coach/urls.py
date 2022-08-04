from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CoachView.as_view(), name='coach'),
    path('<slug:slug>/edit',
         views.CoachEditView.as_view(), name='coach-edit'),
    path('<slug:slug>/delete',
         views.coachDeleteView.as_view(), name='coach-delete'),
]
