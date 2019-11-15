from django.db import models
from django.contrib.auth.models import User
from PIL import Image

GENDER_CHOICES = (
                    ('M', 'Male'),
                    ('F', 'Female'),
                    ('P', 'Prefer not to answer'),
                )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    nickname = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='P')
    bio = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('profile_edit', kwargs={'pk': self.pk})

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
