from django.urls import path
from . import views

urlpatterns = [
    path('school/', views.SchoolView.as_view(), name='school'),
    path('school/<slug:slug>/edit',
         views.SchoolEditView.as_view(), name='school-edit'),
    path('school/<slug:slug>/delete',
         views.SchoolDeleteView.as_view(), name='school-delete'),

    path('group/', views.GroupView.as_view(), name='group'),
    path('group/<slug:slug>/edit', views.GroupEditView.as_view(), name='group-edit'),
    path('<slug:slug>/delete', views.GroupDeleteView.as_view(), name='group-delete'),

    path('timetable/', views.TimetableView.as_view(), name='timetable'),
    path('timetable/<slug:slug>/edit', views.TimetableEditView.as_view(),
         name='timetable-edit'),
    path('timetable/<slug:slug>/delete', views.TimetableDeleteView.as_view(),
         name='timetable-delete'),
]
