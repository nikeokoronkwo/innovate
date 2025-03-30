from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    remote = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number.')])
    location = models.CharField(max_length=255)

class FeedBackRequest(models.Model):
    tags = models.JSONField(default=list)
    html_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class InventoryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name
    
class SupplyRequestTable(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.ForeignKey(InventoryCategory,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Out of stock', 'Out of stock')], 
                              default='Available'
    )
    request_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.first_name} - {self.item_name} {self.status}"
    