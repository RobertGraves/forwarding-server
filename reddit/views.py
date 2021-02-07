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