from django.shortcuts import render

# Create your views here.
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .utils import ListRetrieveUpdateViewSet
from .filters import SlotFilter, ReservationFilter
from .serializers import SlotSerializer, ReservationSerializer
from .models import Slot, Reservation
from .paginators import SlotsSetPagination


class SlotListView(ListRetrieveUpdateViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    authentication_classes = [OAuth2Authentication, ]
    filter_backends = (DjangoFilterBackend,)
    filter_class = SlotFilter
    pagination_class = SlotsSetPagination


class ReservationViewSet(ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [OAuth2Authentication, ]
    filter_backends = (DjangoFilterBackend,)
    filter_class = ReservationFilter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)
