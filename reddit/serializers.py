from .models import *
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model = Comment

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model = Ticker
        depth = 1