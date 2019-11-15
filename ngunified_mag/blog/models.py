from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_img')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
