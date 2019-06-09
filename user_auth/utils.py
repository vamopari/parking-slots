
import requests
from django.conf import settings

from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet


class MultipleFieldPKModelMixin(object):
    """
    Class to override the default behaviour for .get_object for models which have retrieval on fields
    other  than primary keys.
    """
    lookup_field = []
    lookup_url_kwarg = []

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        get_args = {field: self.kwargs[field] for field in
                    self.lookup_field if field in self.kwargs}

        get_args.update({'pk': self.kwargs[field] for field in
                        self.lookup_url_kwarg if field in self.kwargs})
        return get_object_or_404(queryset, **get_args)


class CreateRetrieveUpdateViewSet(GenericViewSet,
                                  mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin):
    pass

class ListRetrieveUpdateViewSet(GenericViewSet,
                                  mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin):
    pass

class RetrieveViewset(GenericViewSet, mixins.RetrieveModelMixin):
    """
    Allows only retrieval of single object.
    """
    pass


def generate_oauth_token(host, username, password):

    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'password',
               'username': username,
               'password': password,
               'client_id': client_id,
               'client_secret': client_secret}

    return (requests.post(settings.SERVER_PROTOCOLS + host + "/o/token/",
                          data=payload, headers=headers))



