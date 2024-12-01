from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from users.serializers import UserRegisterSerialzer
from rest_framework import status
from users.validators import convert_to_lowercase
from users.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import CustomTokenObtainPairSerializer, DocumentDetailsSerializer
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
    

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    def get(self, request):
        return HttpResponseRedirect('http://127.0.0.1:5500/Pharmacy_FrontEnd/index.html')
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email= email).first()
        if user == None:
            return Response({"message": "Invalid Email"}, status= status.HTTP_400_BAD_REQUEST)
        if user and user.check_password(password):
            token = CustomTokenObtainPairSerializer.get_token(user=user)
            return Response({"message":1, "token": token},
                             status=status.HTTP_200_OK)
        elif user and not user.check_password(password):
            return Response({"message": "Invalid Password"}, status= status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invalid Credentials"}, status= status.HTTP_400_BAD_REQUEST)

class HomePageView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
         return Response({'url': 'http://127.0.0.1:5500/Pharmacy_FrontEnd/pages/home.html'})
    
class DocumentView(APIView):
    permission_classes = [IsAuthenticated]
    def upload_file(request):
        if request.method == 'POST' and request.FILES['file']:
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            return JsonResponse({'file_url': uploaded_file_url})
        return JsonResponse({'error': 'No file uploaded'}, status=400)
    def post(self, request):
            section_data = request.data.copy()
            section_data["user"] = request.user
            serializer = DocumentDetailsSerializer(
            data=convert_to_lowercase(section_data),
            context={"request": request},
            )

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
