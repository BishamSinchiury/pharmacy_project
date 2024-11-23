from rest_framework import serializers
from users.models import CustomUser
from users.validators import check_required_fields

from django.core.exceptions import ValidationError


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


