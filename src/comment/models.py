from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now = True, blank = True, null = True)
    
