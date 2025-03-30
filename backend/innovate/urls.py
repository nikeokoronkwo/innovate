from django.urls import path
from . views import AuthView, FeedbackView

urlpatterns = [
    path("api/login/", AuthView.as_view(), name='login'),
    path("api/feedback/", FeedbackView.as_view(), name="feedback"),
    
]