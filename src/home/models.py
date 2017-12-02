from django.db import models
from citizen.models import Citizen

class AnonymousTip(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField()
    userid = models.ForeignKey(Citizen,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_time = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
