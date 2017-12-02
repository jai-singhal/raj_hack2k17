from django.contrib.auth.models import User
from django.db import models


class AnonymousUser(User):
    pass

    class Meta:
        verbose_name = 'Anonymous User'

    def __str__(self):
        return self.username


class AnonymousTip(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField()
    userid = models.ForeignKey(AnonymousUser,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    incident_time = models.DateField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
