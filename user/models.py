from django.db import models
from mega import Mega
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True, null=True)  
    profile_pic_url = models.URLField(max_length=500, blank=True, null=True)  

    def save(self, *args, **kwargs):
        # Save the instance first to get the path
        super().save(*args, **kwargs)
        
        # Only upload if the profile_pic is not the default image
        if self.profile_pic and self.profile_pic.url != '/media/profile_pics/default.jpg':
            self.profile_pic_url = upload_to_mega(self.profile_pic.path)
            # Optionally delete the local file if needed
            self.profile_pic.delete(save=False)

        # Save the instance again to update the profile_pic_url
        super().save(*args, **kwargs)  


def upload_to_mega(file_path):
    mega = Mega()
    mega.login(settings.MEGA_EMAIL, settings.MEGA_PASSWORD)
    uploaded_file = mega.upload(file_path)
    public_url = mega.get_upload_link(uploaded_file)
    return public_url
