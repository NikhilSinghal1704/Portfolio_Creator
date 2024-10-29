from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django_cleanup import cleanup

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/')
    phone_no = models.IntegerField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return static('images/default_avatar.png')
