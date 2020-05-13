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
    path('stocks', views.stocks, name='stocks'),
    path('closed', views.closed, name='closed'),
    #CRUD endpoints
    path('centerview', CenterView.as_view(), name='center_view'),
    path('centerview/<str:center_name>', CenterView.as_view(), name='center_view'),
    path('userview', UserView.as_view(), name='center_view'),
    path('userview/<str:username>', UserView.as_view(), name='center_view'),
    path('entryview', EntryView.as_view(), name='center_view'),
    path('entryview/<str:mobile>', EntryView.as_view(), name='center_view'),
    path('getcurrententries', get_current_entries, name='get_current_entries'),
    path('getclosedentries', get_closed_entries, name='get_closed_entries'),
    path('markasdone', mark_as_done, name='mark_as_done'),
    path('markasdoneimage', UploadView.as_view(), name='UploadView'),
    path('updatetotalstock', update_stock_count, name='update_stock_count'),
    # path('updatecenterstock', update_center_stock_count, name='update_center_stock_count'),
    path('addshipment', add_shipment, name='add_shipment'),
    path('markshipment', mark_shipments, name='mark_shipments'),
    path('getshipments', get_shipments, name='get_shipments'),
]

initialize_centers()
