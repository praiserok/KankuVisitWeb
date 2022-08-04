from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.group, name='group'),
    path('<slug:slug>/edit', views.GroupEditView.as_view(), name='group-edit'),
    path('<slug:slug>/delete', views.groupDelete, name='group-delete'),

]
