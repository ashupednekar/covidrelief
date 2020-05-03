from django.urls import path
from app.extras import initialize_centers
from .endpoints import *
from . import views

urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    #other dashboard pages
    path('centers', views.centers, name='centres'),
    #CRUD endpoints
    path('centerview', CenterView.as_view(), name='center_view'),
    path('centerview/<str:center_name>', CenterView.as_view(), name='center_view'),
]

initialize_centers()