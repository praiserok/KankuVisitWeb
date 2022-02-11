from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.timetable, name='timetable'),
    path('<slug:slug>/edit', views.TimetableEditView.as_view(),
         name='timetable-edit'),
    path('<slug:slug>/delete', views.timetableDelete, name='timetable-delete'),

]
