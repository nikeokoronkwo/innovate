from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthView, FeedbackViewSet, SupplyRequestView

router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include(router.urls)),
        path('login/', AuthView.as_view(), name='login'),
        path('supply-request/', SupplyRequestView.as_view(), name='supply-request'),
    ])),
]