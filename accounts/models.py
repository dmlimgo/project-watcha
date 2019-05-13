from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    from_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='to_user')

class Profile(models.Model):
    nickname = models.CharField(max_length=50)
    introduction = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)