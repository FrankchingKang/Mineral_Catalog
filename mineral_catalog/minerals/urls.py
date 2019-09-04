from django.urls import path
from . import views

urlpatterns = [
    path('',views.minerals_create),
]
