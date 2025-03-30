from django.contrib import admin
from . models import CustomUser, FeedBackRequest
# Register your models here.

admin.site.register(CustomUser)
@admin.register(FeedBackRequest)
class FeedBackRequestAdmin(admin.ModelAdmin):
    list_display = ("tags","html_text", "created_at")