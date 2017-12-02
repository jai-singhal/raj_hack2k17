from django.db import models
from police.models import Police
from citizen.models import Citizen

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now = True, blank = True, null = True)
    user1 = models.ForeignKey(Police, null = True, blank = True)
    user2 = models.ForeignKey(Citizen, null = True, blank = True)
