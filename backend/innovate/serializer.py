from rest_framework import serializers
from .models import FeedBackRequest

class FeedBackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackRequest
        fields = '__all__'
