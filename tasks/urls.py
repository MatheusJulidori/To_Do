from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList),
    path('username/<str:name>', views.userName),
]