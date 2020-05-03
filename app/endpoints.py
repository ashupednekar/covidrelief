from rest_framework import generics, mixins
from .serializers import *


class CenterView(
    generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView,
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin
    ):

    queryset = Centers.objects.all()
    serializer_class = CenterSerializer
    lookup_field = 'center_name'

    def post(self, request):
        return self.create(request)

    def get(self, request, center_name=None):
        if center_name:
            return self.retrieve(request, center_name)
        else:
            return self.list(request)

    def put(self, request, center_name=None):
        return self.update(request, center_name)

    def delete(self, request, center_name=None):
        return self.destroy(request, center_name)