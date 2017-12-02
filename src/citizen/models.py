from django.contrib.auth.models import User
from django.db import models


class Citizen(User):
    contact = models.CharField(max_length=11)
    aadhaar  = models.CharField(max_length=12)
    bhamshah = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Citizen'

    def __str__(self):
        return self.get_full_name()
