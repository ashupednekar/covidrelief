import os

from rest_framework import generics, mixins
from .serializers import *
from localusers.serializers import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

import boto3
s3 = boto3.client('s3')

class EntryView(
    generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView, generics.RetrieveAPIView,
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin
    ):

    queryset = Entries.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'mobile'

    def post(self, request):
        return self.create(request)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['actor'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, mobile=None):
        if mobile:
            return self.retrieve(request, mobile)
        else:
            return self.list(request)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        res = serializer.data
        res['date_received'] = res['date_received'].strftime("%m/%d/%Y")
        print(res)
        return Response(res)

    def put(self, request, mobile=None):
        return self.update(request, mobile)

    def delete(self, request, mobile=None):
        return self.destroy(request, mobile)


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
        return Response(list(entries.values()), status=status.HTTP_200_OK)
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='N', center=request.user.center)
        return Response(list(entries.values()), status=status.HTTP_200_OK)
    else:
        return Response({'messsage': 'Invalid Role'})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_closed_entries(request):
    if request.user.role == 'admin':
        entries = Entries.objects.filter(closed='Y')
        return Response(list(entries.values()), status=status.HTTP_200_OK)
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='Y', center=request.user.center)
        return Response(list(entries.values()), status=status.HTTP_200_OK)
    else:
        return Response({'messsage': 'Invalid Role'})

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def mark_as_done(request):
    if request.user.role in ['admin', 'manager']:
        for entry in request.data.get('tomark').split(','):
            Entries.objects.filter(mobile=entry).update(closed='Y')
        return Response({'messsage': 'Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'messsage': 'Invalid Role'})

import boto3
s3 = boto3.client('s3')

class UploadView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()

    def post(self, request):
        return self.create(request)

    def create(self, request, *args, **kwargs):
        if request.user.role in ['admin', 'manager']:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print('DEBUG: ', serializer.data)
            fn = 'img/' + serializer.data['fn'].split('/')[-1]
            s3.upload_file(fn, 'whatsapp-img', 'covidrelief/'+fn, ExtraArgs={'ContentType': "image/png", 'ACL': "public-read"})
            os.system('rm '+ fn)
            url = 'https://whatsapp-img.s3.amazonaws.com/covidrelief/' + fn
            for entry in request.data.get('tomark').split(','):
                Entries.objects.filter(mobile=entry).update(closed='Y', image=url)
            return Response({"message": "success", "url": url}, status=status.HTTP_200_OK, headers=headers)
        else:
            return Response({'messsage': 'Invalid Role'})

    def get(self, request):
        return self.list(request)