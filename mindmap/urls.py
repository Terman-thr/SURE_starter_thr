from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('', views.get_index)
]