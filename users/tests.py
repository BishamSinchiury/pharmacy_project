# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APITestCase
# from users.models import CustomUser
# from users.serializers import UserRegisterSerialzer
# from django.contrib.auth import get_user_model

# # Create your tests here.
# class registerAPItest(TestCase):
#     def test_valid_registration(self):
#         data = {
#             "username":"John Doe",
#             "email":"john@example.com",
#             "password":"john123",
#             "password2":"john123"
#         }

#         serializer = UserRegisterSerialzer(data = data)
#         self.assertTrue(serializer.is_valid())
#         user = serializer.save()

#         self.assertEqual(user.username, data['username'])
#         self.assertEqual(user.email, data['email'])
#         self.assertTrue(user.check_password(data['password']))

#     def test_password_mistmatch(self):
#         data = {
#             "username":"John Doe",
#             "email":"john@example.com",
#             "password":"john123",
#             "password2":"john1234"
#         }

#         serializer = UserRegisterSerialzer(data = data)

#         self.assertFalse(serializer.is_valid())
#         self.assertIn('error', serializer.errors)
#         self.assertEqual(serializer.errors['error'][0], 'passwords must match')
    
#     def test_missing_required_fields(self):
#         """
#         Test that the required fields are validated properly.
#         """
#         data = {
#             "username": "testuser",
#             "email": "testuser@example.com",
#             "password": "strongpassword123"
#             # Missing password2
#         }
        
#         serializer = UserRegisterSerializer(data=data)
        
#         # Ensure the serializer is not valid due to missing password2
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('password2', serializer.errors)  # Ensure password2 is required

#     def test_user_creation(self):
#         """
#         Test user creation when data is valid.
#         """
#         data = {
#             "username": "testuser",
#             "email": "testuser@example.com",
#             "password": "strongpassword123",
#             "password2": "strongpassword123"
#         }
        
#         serializer = UserRegisterSerialzer(data=data)
        
#         # Ensure the serializer is valid
#         self.assertTrue(serializer.is_valid())
        
#         # Create the user
#         user = serializer.save()
        
#         # Check that user was created
#         self.assertEqual(CustomUser.objects.count(), 1)
#         self.assertEqual(user.username, "testuser")
#         self.assertEqual(user.email, "testuser@example.com")

#     def test_user_creation_with_existing_email(self):
#         """
#         Test user creation fails with an existing email.
#         """
#         data1 = {
#             "username": "user1",
#             "email": "duplicate@example.com",
#             "password": "strongpassword123",
#             "password2": "strongpassword123"
#         }
        
#         # Create the first user
#         UserRegisterSerialzer(data=data1).save()

#         # Try to create a second user with the same email
#         data2 = {
#             "username": "user2",
#             "email": "duplicate@example.com",  # Same email
#             "password": "strongpassword123",
#             "password2": "strongpassword123"
#         }
        
#         serializer = UserRegisterSerialzer(data=data2)
        
#         # Ensure the serializer is invalid due to duplicate email
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('email', serializer.errors) 

from django.contrib.auth.models import UserManager