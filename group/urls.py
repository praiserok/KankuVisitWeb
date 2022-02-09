from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.group, name='group'),
    path('<int:pk>/edit', views.GroupEditView.as_view(), name='group-edit'),
    path('<int:pk>/delete', views.groupDelete, name='group-delete'),

]
