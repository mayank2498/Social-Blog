from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User,null=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=100,default="Codeutsav")
    description = models.CharField(max_length=1000,default="No desciption")
    allow = models.BooleanField(default=False)
    image = models.ImageField()
    designation = models.CharField(max_length=50,default="Student")
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.author + self.title




























