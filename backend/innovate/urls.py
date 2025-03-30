from django.urls import path
from . views import AuthView, FeedbackView

urlpatterns = [
    path("login/", AuthView.as_view(), name='login'),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    
]