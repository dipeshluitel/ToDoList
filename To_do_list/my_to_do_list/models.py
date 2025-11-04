from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class To_do_list(models.Model):
    listed = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.listed

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)