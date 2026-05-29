from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser ):
    full_name = models.CharField(max_length = 255)
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    photo = models.ImageField(upload_to='Profiles',blank=True, null=True)

    def __str__(self):
        return self.user.username