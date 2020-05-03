from django.urls import path
from app.extras import initialize_centers
from .endpoints import *
from . import views

urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    #other dashboard pages
    path('centers', views.centers, name='centres'),
    path('assign', views.assign, name='assign'),
    path('entries', views.entries, name='entries'),
    path('closed', views.closed, name='closed'),
    #CRUD endpoints
    path('centerview', CenterView.as_view(), name='center_view'),
    path('centerview/<str:center_name>', CenterView.as_view(), name='center_view'),
    path('userview', UserView.as_view(), name='center_view'),
    path('userview/<str:username>', UserView.as_view(), name='center_view'),
    path('entryview', EntryView.as_view(), name='center_view'),
    path('entryview/<str:mobile>', EntryView.as_view(), name='center_view'),
    path('getcurrententries', get_current_entries, name='get_current_entriesK'),
    path('getclosedentries', get_closed_entries, name='get_closed_entries'),
]

initialize_centers()
