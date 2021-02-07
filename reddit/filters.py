
from django_filters.rest_framework import FilterSet,NumberFilter,BooleanFilter,CharFilter
from .models import *

# class AllDjangoFilterBackend(filters.FilterSet):
#     """
#     A filter backend that uses django-filter.
#     """

#     def get_filter_class(self, view, queryset=None):
#         """
#         Return the django-filters `FilterSet` used to filter the queryset.
#         """
#         filter_class = getattr(view, 'filter_class', None)
#         filter_fields = getattr(view, 'filter_fields', None)

#         if filter_class or filter_fields:
#             return super(AllDjangoFilterBackend, self).get_filter_class(self, view, queryset)

#         class AutoFilterSet(self.default_filter_set):
#             class Meta:
#                 model = queryset.model
#                 fields = None

#         return AutoFilterSet



class TickerFilterSet(FilterSet):
    class Meta:
        model = Ticker
        fields={
            'comment':['exact'],
            'comment__body':['iexact','icontains'],
            'comment__name':['iexact','icontains'],
            'ticker':['icontains','iexact'],
            'timestamp':['month','year','gte','lte','lt','gt'],
            'update':['month','year','gte','lte','lt','gt'],
            'id':['exact']
        }
class CommentFilterSet(FilterSet):
    class Meta:
        model = Comment
        fields={
            'body':['iexact','icontains'],
            'comment__name':['iexact','icontains'],
            'timestamp':['month','year','gte','lte','lt','gt'],
            'update':['month','year','gte','lte','lt','gt'],
            'id':['exact']
        }