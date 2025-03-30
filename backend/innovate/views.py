from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializer import FeedBackRequestSerializer
from django.contrib.auth import authenticate

class AuthView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email = email, password = password)

        if email == 'bright.andohh@gmail.com' and password == '12345':
            return Response({'message': 'Login successful', 'email': email, 'firstname': user.first_name, 'lastname': user.last_name}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
class FeedbackView(APIView):
    def post(self, request):
        serializer = FeedBackRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)