
from rest_framework import mixins
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

class ListRetrieveUpdateViewSet(GenericViewSet,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin):
    pass
