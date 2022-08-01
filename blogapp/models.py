
from email.policy import default
from django.db import models
from tinymce import models as tinymce_models

from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    post_title=models.CharField(max_length=50,null=False)
    post_summary=models.TextField()
    post_body=tinymce_models.HTMLField()
    post_image =models.ImageField(upload_to='post_images/', null=True)
    

    def __str__(self) -> str:
        return self.post_title

class Comment(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    comment_body=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment_body


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    ph_no=models.CharField(max_length=50)
    text=models.TextField()


    def __str__(self) -> str:
        return self.name
    

  

        