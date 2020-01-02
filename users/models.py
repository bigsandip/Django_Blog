from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # importing pillow Library to resize img
# Create your models here.


class Profile(models.Model):  # now register Profile to admin on admin.py
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one user has only one profile so oneTo One
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # pip install pillow to use image or imagefiels

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)  # Running the save() Of parent class.. save() method already exists in parent class..It's function is to automatically save the anything when it is called
        img = Image.open(self.image.path)  # so we are overriding save() method

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
