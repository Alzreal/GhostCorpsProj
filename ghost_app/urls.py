from turtle import st
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('messages', views.messages),
    path('add_job', views.add_job),
    path('delete_job/<int:job_id>', views.delete_job),
    path('equipment', views.equipment),
    path('tobins', views.tobins),
    path('founding', views.founding),
    path('EditPage', views.EditPage),
    path('EditAccount', views.EditAccount),
    path('medicorps', views.medicorps),
]
