from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from users.models import CustomUser, Documents
from users.validators import check_required_fields
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserRegisterSerialzer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def validate(self, data):
        request_method = self.context["request"].method
        if data['password'] !=  data['password2']:
            raise ValidationError(
                    {"error": "passwords must match"}
            )
        if request_method == "POST":
            required_fields = self.Meta.fields
            required_fields.append('password2')
            check_required_fields(data, required_fields)
        
        return data
    

    def create(self, validated_data):
        validated_data.pop('password2')  
        return CustomUser.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)
        token["is_staff"] = user.is_staff
        token["is_manager"] = user.is_manager
        token["is_superuser"] = user.is_superuser
        return str(token.access_token)

# Serializer for handling specific document details related to an individual
class DocumentDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for managing specific document details of an individual.
    """
    class Meta:
        model = Documents
        fields = [
            "passport_sized_photo",      # Passport-sized photograph of the individual
            "signature",                 # Individual's signature
            "citizenship_front",         # Front image of the citizenship document
            "citizenship_back",          # Back image of the citizenship document
            "location_map",              # Location map related to the individual
            "selfie_with_citizenship",   # Selfie of the individual holding their citizenship document
            "user"        
        ]

    def validate(self, data):
        """
        Validates required fields for POST requests.

        Ensures that all fields listed in `Meta.fields` are present in the request 
        data when creating new document records.
        """
        request_method = self.context["request"].method

        # Perform validation only for POST requests
        if request_method == "POST":
            # Validate that all required fields are provided in the request data
            check_required_fields(data, self.Meta.fields)

        return data