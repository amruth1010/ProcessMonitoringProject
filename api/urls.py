from django.urls import path
from . import views

urlpatterns = [
    path('receive/', views.receive_process),
    path('latest/', views.latest_processes),
]
