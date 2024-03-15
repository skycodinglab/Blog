
from datetime import datetime
from django.db import models
from custom_user.models import CustomUser

class Category(models.Model):
    name   =   models.CharField(max_length=50, null=True)
    banner_img = models.ImageField(upload_to='category/')
    slug    =   models.SlugField(default="", max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Category'
    def __str__(self):
        return self.name

class Tags(models.Model):
    name   =   models.CharField(max_length=50, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural = 'Tags'
    def __str__(self):
        return self.name
    
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE, null=True)
    post_title = models.CharField(max_length=200, null=True)
    slug    =   models.SlugField(default="", max_length=100, null=False)
    post_img = models.ImageField(upload_to='post_image/')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural = 'Post'
    def __str__(self):
        return self.post_title

class CommentsPost(models.Model):
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'PostComment'
    def __str__(self):
        return self.comment
    
class ReplyPost(models.Model):
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    comments = models.ForeignKey(CommentsPost, on_delete=models.CASCADE)
    reply_comments = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ReplyPost'
  


   

   
