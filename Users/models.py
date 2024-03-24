from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics.jpg')
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user_name.username
