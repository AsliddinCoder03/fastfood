from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class EmailCode(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    code = models.CharField(max_length=7, unique=False)