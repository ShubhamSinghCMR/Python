from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class Post(models.Model):
    text=models.CharField(max_length=140,blank=False,null=False)
    image=ImageField()
    description=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text