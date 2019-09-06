from django.urls import path
from . import views

urlpatterns = [
    path('',views.minerals_create),
    path('list', views.mineral_list)
]
