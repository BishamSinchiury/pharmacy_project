from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, permissions
from users.serializers import UserRegisterSerialzer
from rest_framework import status
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        serializer = UserRegisterSerialzer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "user created sucessfully",
                "status":True,
                "data": serializer.data
            }, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return redirect('http://127.0.0.1:5500/Pharmacy_FrontEnd/index.html')
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = CustomUser.objects.filter(email= email).first()
        if user == None:
            return Response({"message": "Invalid Email"}, status= status.HTTP_400_BAD_REQUEST)
        if user and user.check_password(password= password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)
        elif user and not user.check_password(password= password):
            return Response({"message": "Invalid Password"}, status= status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invalid Credentials"}, status= status.HTTP_400_BAD_REQUEST)

class HomePageView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message":"This is acceses"})

