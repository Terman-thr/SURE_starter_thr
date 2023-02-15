from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('', views.get_index),
    path('api/save/<int:mapid>/', views.save_api),
    path('map/<int:id>/', views.get_map),
    path('api/create/', views.create_map),
]
