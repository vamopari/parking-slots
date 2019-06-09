from django.conf.urls import url
from django.urls import path

from .views import SlotListView, ReservationViewSet



urlpatterns = [

    path('slot/', SlotListView.as_view({'get': 'list'})),
    path('slot/<int:pk>/', SlotListView.as_view({'get': 'retrieve'})),

    path('reservation/', ReservationViewSet.as_view({'get': 'list', 'post':'create'})),
    path('reservation/<int:pk>/', ReservationViewSet.as_view({'get': 'retrieve', 'put': 'update'}))
]
