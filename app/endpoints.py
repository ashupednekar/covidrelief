from rest_framework import generics, mixins
from .serializers import *
from localusers.serializers import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class EntryView(
    generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView,
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin
    ):

    queryset = Entries.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'mobile'

    def post(self, request):
        return self.create(request)

    def get(self, request, mobile=None):
        if mobile:
            return self.retrieve(request, mobile)
        else:
            return self.list(request)

    def put(self, request, mobile=None):
        return self.update(request, mobile)

    def delete(self, request, mobile=None):
        return self.destroy(request, username)


class UserView(
    generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView,
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin
    ):

    queryset = LocalUser.objects.all()
    serializer_class = LocalUserSerializer
    lookup_field = 'username'

    def post(self, request):
        return self.create(request)

    def get(self, request, username=None):
        if username:
            return self.retrieve(request, username)
        else:
            return self.list(request)

    def put(self, request, username=None):
        return self.update(request, username)

    def delete(self, request, username=None):
        return self.destroy(request, username)


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


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_current_entries(request):
    if request.user.role == 'admin':
        entries = Entries.objects.filter(closed='N')
        return list(entries.values())
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='N', center=request.user.center)
        return list(entries.values())
    else:
        raise NotImplementedError


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_closed_entries(request):
    if request.user.role == 'admin':
        entries = Entries.objects.filter(closed='Y')
        return list(entries.values())
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='Y', center=request.user.center)
        return list(entries.values())
    else:
        raise NotImplementedError

