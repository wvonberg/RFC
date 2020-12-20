from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def validator(self, form):
        errors = {}
        if len(form['content']) < 3:
            errors['length'] = "message must be at least 3 chars!"
        return errors

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="x_user_post", on_delete=models.CASCADE)
    body = models.TextField()
    #image = models.ImageField(null=True, blank=True, upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

    def __str__(self):
        return self.title + ' | ' + self.author

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RequestManager(models.Manager):
    def validator(self, form):
        errors = {}
        if len(form['content']) < 3:
            errors['length'] = "message must be at least 3 chars!"
        return errors

class Request(models.Model):
    bot_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="x_user_request", on_delete=models.CASCADE)
    body = models.TextField()
    #image = models.ImageField(null=True, blank=True, upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RequestManager()
    
    def __str__(self):
        return self.bot_name + ' | ' + self.owner


    
class Support(models.Model):
    message=models.TextField()
    requestor=models.ForeignKey(User,related_name="requests", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
