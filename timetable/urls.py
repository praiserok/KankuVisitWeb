from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.timetable, name='timetable'),
    path('<int:pk>/edit', views.TimetableEditView.as_view(), name='timetable-edit'),
    path('<int:pk>/delete', views.timetableDelete, name='timetable-delete'),

]
