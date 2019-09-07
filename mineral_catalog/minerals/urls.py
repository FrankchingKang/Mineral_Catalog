from django.urls import path
from . import views

app_name = 'minerals'

urlpatterns = [
    path('',views.minerals_create),
    path('list', views.mineral_list, name="list"),
    path('detail/<int:pk>', views.mineral_detail, name="detail")
]
