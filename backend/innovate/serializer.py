from rest_framework import serializers
from .models import FeedBackRequest, SupplyRequestTable, InventoryCategory

class FeedBackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackRequest
        fields = ['id', 'tags', 'html_text', 'created_at'] 

class InventoryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCategory
        fields = ['id', 'name']

class SupplyRequestSerializer(serializers.ModelSerializer):
    item_name = InventoryCategorySerializer() 

    class Meta:
        model = SupplyRequestTable
        fields = ['id', 'user', 'item_name', 'quantity', 'status', 'request_date']