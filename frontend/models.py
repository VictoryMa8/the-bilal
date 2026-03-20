from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

roles = [(1, "Reader"), (2, "Contributor"), (3, "Journalist"), (4, "Admin")]
post_types = [(1, "Question"), (2, "Analysis"), (3, "Opinion"), (4, "Other")]
# Create your models here.
class User(AbstractUser):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.IntegerField(choices=roles, default=1)
    is_verified = models.BooleanField(default=False)
    last_active = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")

    def __str__(self):
        return self.username
    
class Cycle(models.Model): # Cycles are intervals of time that given topics are associated with
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Topic(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    cycle_id = models.ForeignKey(Cycle, on_delete=models.CASCADE) # Topics are associated with a given cycle
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="topic_images/")
    
class Post(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE) # Posts must have authors (contributer users and above)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE) # Posts must pertain to a certain topic
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    endorsements = models.IntegerField(default=0)
    post_type = models.IntegerField(choices=post_types, default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="post_images/")

class Article(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=20000)
    endorsements = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_1 = models.ImageField(null=True, blank=True, upload_to="article_images/")
    image_2 = models.ImageField(null=True, blank=True, upload_to="article_images/")

class Comment(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=5000)
    endorsements = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Poll(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    cycle_id = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
