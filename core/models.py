from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    id_user = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profileimage = models.ImageField(upload_to='profileimgs', default='blank-profile-picture.png')
    location = models.CharField(max_length=120, null=True, blank=True)
    private = models.BooleanField(default=False)
    allowcomments = models.BooleanField(default=True)
    notificationson = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    posts = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    dposts = models.CharField(max_length=120, default='0')
    dfollowers = models.CharField(max_length=120, default='0')
    dfollowing = models.CharField(max_length=120, default='0')
    
    def __str__(self):
        return self.user.username # type: ignore

class Follow(models.Model):
    user = models.CharField(max_length=120)
    followed = models.CharField(max_length=120)
    
    def __str__(self):
        return f"{self.user} followed {self.followed}"
     

class Post(models.Model):
    user = models.CharField(max_length=120)
    pimg = models.ImageField(upload_to='profileimgs', default='blank-profile-picture.png')
    file = models.FileField(upload_to='posts', blank=True, null=True)
    link = models.CharField(max_length=300, blank=True, null=True)
    caption = models.TextField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    
    def __str__(self):
        return f"{self.user}'s post"