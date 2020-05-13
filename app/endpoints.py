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
        stocks = Stocks.objects.all()
        count = list(stocks.values())[0]['count']
        if list(stocks):
            Stocks.objects.update(count=count-1)
        else:
            return Response({'message': 'no stocks available'}, status=status.HTTP_402_PAYMENT_REQUIRED)
        center_stocks = Centers.objects.filter(center_name=serializer.validated_data['center'])
        stock_count = list(center_stocks.values())[0]['stock_count']
        if stock_count > 0:
            center_stocks.update(stock_count=stock_count-1)
            self.perform_create(serializer)
        else:
            return Response({'message': 'no stocks available'}, status=status.HTTP_402_PAYMENT_REQUIRED)
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
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
        return Response(res, status=status.HTTP_200_OK)
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='N', center=request.user.center)
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
        return Response(res, status=status.HTTP_200_OK)
    else:
        return Response({'messsage': 'Invalid Role'})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_closed_entries(request):
    if request.user.role == 'admin':
        entries = Entries.objects.filter(closed='Y')
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
        return Response(res, status=status.HTTP_200_OK)
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='Y', center=request.user.center)
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
        return Response(res, status=status.HTTP_200_OK)
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


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def update_stock_count(request):
    if request.method == 'POST':
        try:
            stock_count = request.data.get('stock_count')
            if list(Stocks.objects.all()):
                Stocks.objects.update(count=stock_count)
            else:
                Stocks.objects.create(count=stock_count)
            return Response({'message': 'stock updated successfully', 'count': stock_count}, status=status.HTTP_200_OK)
        except Exception as e:
            print('..error..', e)
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def update_center_stock_count(request):
#     if request.method == 'POST':
#         try:
#             stock_count = request.data.get('stock_count')
#             center = request.data.get('center')
#             total_stocks = list(Stocks.objects.all().values())[0].get('count')
#             available_stocks = total_stocks
#             for x in list(Centers.objects.all().values()):
#                 available_stocks -= x['stock_count']
#             if int(stock_count) <= int(available_stocks):
#                 Centers.objects.filter(center_name=center).update(stock_count=stock_count)
#                 return Response({'message': 'stock at the center updated successfully', 'count': stock_count}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'insufficient stocks'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             print('..error..', e)
#             return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_shipment(request):
    if request.method == 'POST':
        try:
            stock_count = request.data.get('stock_count')
            center = request.data.get('center')
            total_stocks = list(Stocks.objects.all().values())[0].get('count')
            available_stocks = total_stocks
            for x in list(Centers.objects.all().values()):
                available_stocks -= x['stock_count']
            if int(stock_count) <= int(available_stocks):
                # Centers.objects.filter(center_name=center).update(stock_count=stock_count)
                Shipments.objects.create(sender=request.user, amount=stock_count, center=center)
                return Response({'message': 'stock at the center updated successfully', 'count': stock_count}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'insufficient stocks'}, status=status.HTTP_200_OK)
        except Exception as e:
            print('..error..', e)
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def mark_shipments(request):
    if request.method == 'POST':
        try:
            shipment_id = request.data.get('shipment_id')
            package = Shipments.objects.filter(shipment_id=shipment_id)
            if list(package.values()):
                amount = list(package.values())[0]['amount']
            else:
                return Response({'message': 'ERROR'}, status=status.HTTP_200_OK)
            center_name = list(package.values())[0]['center']
            center = Centers.objects.filter(center_name=center_name)
            center.update(stock_count=list(center.values())[0]['stock_count']+amount)
            package.update(delivered='Y')
            return Response({'message': 'Marked as delivered'}, status=status.HTTP_200_OK)
        except Exception as e:
            print('..error..', e)
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def get_shipments(request):
    if request.method == 'POST':
        try:
            center = request.data.get('center')
            if center:
                res = list(Shipments.objects.filter(center=center).values())
            else:
                res = list(Shipments.objects.all().values())
            return Response(res, status=status.HTTP_200_OK)
        except Exception as e:
            print('..error..', e)
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)