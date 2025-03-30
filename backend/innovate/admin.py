from django.contrib import admin
from . models import CustomUser, FeedBackRequest
from django.contrib import admin
from .models import SupplyRequestTable
# Register your models here.

admin.site.register(CustomUser)
@admin.register(FeedBackRequest)
class FeedBackRequestAdmin(admin.ModelAdmin):
    list_display = ("tags","html_text", "created_at")

@admin.register(SupplyRequestTable)
class SupplyRequestTableAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_name', 'quantity', 'status', 'request_date')
    list_filter = ('status', 'request_date')
    search_fields = ('user_username', 'item_name')
