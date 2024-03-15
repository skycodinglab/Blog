from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .manager import CustomUsermanager

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'),unique = True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profile_images")
    
    REQUIRED_FIELDS = ['email',]
    objects = CustomUsermanager()

    def __str__(self):
        return self.email
    
    
  