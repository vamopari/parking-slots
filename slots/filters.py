import json

import django_filters
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework.exceptions import ValidationError

from .models import Slot, Reservation

class SlotFilter(django_filters.FilterSet):

    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')

    day = django_filters.DateFilter(method='get_slot_by_day')

    location = django_filters.CharFilter(method='get_location', help_text="""json as: {
            "longitude": float <longitude>,
            "latitude": float <latitude> (),
            "radius": integer (default to 5)
        }
        """)

    def get_location(self, queryset, name, location):
        if location:
            try:
                location_json = json.loads(location)
                assert 'longitude' in location
            except (ValueError, AssertionError) as e:
                raise ValidationError(
                    'location must be json as {"longitude": <float>, "latitude": <float>}')
            import pdb
            pdb.set_trace()
            user_location = Point(float(location_json.get('longitude')),
                                  float(location_json.get('latitude')), srid=4326)
            radius = location_json.get('radius', 10)
            return queryset.filter(location__distance_lt=(user_location, Distance(km=radius)))
        return queryset

    def get_slot_by_day(self, queryset, name, day):
        if day:
            return queryset.filter(day=day)
        return queryset


    class Meta:
        model = Slot
        fields = ['status', 'day', 'location']


class ReservationFilter(django_filters.FilterSet):


    day = django_filters.DateFilter(method='get_reservation_by_day')

    user = django_filters.NumberFilter()

    is_cancelled = django_filters.BooleanFilter()

    def get_reservation_by_day(self, queryset, name, day):
        if day:
            return queryset.filter(day=day)
        return queryset


    class Meta:
        model = Reservation
        fields = ['day']
