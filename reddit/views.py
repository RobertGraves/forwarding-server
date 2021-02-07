from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from .serializers import *
from .pagination import *
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.db.models import Count

class CommentViewSet(ListModelMixin,RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes      = [AllowAny]
    serializer_class        = CommentSerializer
    pagination_class        = StandardResultsSetPagination
    filter_backends         = [OrderingFilter,DjangoFilterBackend]
    ordering_fields         = '__all__'
    ordering                = ['-id']
    # filterset_fields        = "__all__"
    filterset_class         = CommentFilterSet
    queryset                = Comment.objects.all()


class TickerViewSet(ListModelMixin,RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes      = [AllowAny]
    serializer_class        = TickerReadSerializer
    pagination_class        = StandardResultsSetPagination
    filter_backends         = [DjangoFilterBackend,OrderingFilter]
    ordering_fields         = '__all__'
    ordering                = ['-id']
    # filterset_fields        = "__all__"
    filterset_class         = TickerFilterSet
    queryset                = Ticker.objects.all().select_related('comment')



class HotView(APIView):
    # from .utils import aggregate_tickers
    # permission_classes      = [AllowAny]
    # serializer_class        = AggregateTickerSerializer
    # pagination_class        = StandardResultsSetPagination
    # filter_backends         = [DjangoFilterBackend,OrderingFilter]
    # ordering_fields         = '__all__'
    # queryset = Ticker.objects.values('ticker').order_by('ticker').annotate(count=Count('ticker')).order_by('-count')
    def get(self,request,*args,**kwargs):
        ##TODO sanitize to allow time since epoch or strftime formats?
        start= kwargs.get('start',datetime.now()-relativedelta(days=1))
        end = kwargs.get('end',datetime.now())
        # data = aggregate_tickers(start_date,end_date)
        return Response(Ticker.objects.filter(timestamp__gte=start,timestamp__lte=end).values('ticker').order_by('ticker').annotate(count=Count('ticker')).order_by('-count'),status=200)