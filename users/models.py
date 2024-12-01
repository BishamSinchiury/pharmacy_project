from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from users.validators import get_unique_filename, validate_image_file_extension
import uuid



# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_manager', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email=email)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        ordering = ['-created_at']

    def __str__(self):
        return self.username
    

class Documents(models.Model):
    user = models.OneToOneField(
        "CustomUser", on_delete=models.CASCADE, related_name="documents"
    )
    passport_sized_photo = models.ImageField(
        upload_to=get_unique_filename,
        validators=[validate_image_file_extension],
        blank=True,
        null=True,
    )
    signature = models.ImageField(
        upload_to=get_unique_filename,
        validators=[validate_image_file_extension],
        blank=True,
        null=True,
    )
    citizenship_front = models.ImageField(
        upload_to=get_unique_filename,
        validators=[validate_image_file_extension],
        blank=True,
        null=True,
    )
    citizenship_back = models.ImageField(
        upload_to=get_unique_filename,
        validators=[validate_image_file_extension],
        blank=True,
        null=True,
    )
    location_map = models.ImageField(
        upload_to=get_unique_filename,
        validators=[validate_image_file_extension],
        blank=True,
        null=True,
    )
    selfie_with_citizenship = models.ImageField(
        upload_to=get_unique_filename,
        validators=[validate_image_file_extension],
        blank=True,
        null=True,
    )
    is_draft_docs = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Documents for {self.individual.first_name} {self.individual.last_name}"