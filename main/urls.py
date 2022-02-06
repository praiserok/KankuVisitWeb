from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexVisit, name='visit'),
    path('about', views.about, name='about'),
    path('belt', views.belt, name='belt'),

    path('coach', views.coach, name='coach'),
    path('coach/<int:coach_id>/', views.coachEdit, name='coachedit'),
    path('coach/<int:coach_id>/delete', views.delete, name='coachdDelete'),

    path('sportsman', views.sportsman, name='sportsman'),
    path('sportsman/<int:sportsman_id>/',
         views.sportsmanEdit, name='sportsmanEdit'),
    path('sportsman/<int:sportsman_id>/delete',
         views.delete, name='sportsmanDelete'),

    path('school', views.school, name='school'),
    path('school/<int:school_id>/', views.schoolEdit, name='schooledit'),
    path('school/<int:school_id>/delete',
         views.delete, name='schoolDelete'),
]
