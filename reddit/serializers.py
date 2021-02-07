from .models import *
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model = Comment

class TickerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model = Ticker
class TickerReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model = Ticker
        depth = 1

class AggregateTickerSerializer(serializers.Serializer):
    class Meta:
        fields="__all__"