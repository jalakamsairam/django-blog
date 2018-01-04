from django.db import models
from django.contrib.auth.models import User
class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
