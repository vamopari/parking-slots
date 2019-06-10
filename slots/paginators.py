from rest_framework.pagination import  LimitOffsetPagination


class SlotsSetPagination(LimitOffsetPagination):
    default_limit = 1000000
    max_limit = None
