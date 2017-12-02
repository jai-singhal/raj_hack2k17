from django.contrib.auth.models import User
from django.db import models


class Citizen(User):
    contact = models.CharField(max_length=11)
    aadhaar  = models.CharField(max_length=12)
    bhamashah = models.CharField(max_length=12)
    dob = models.DateField()

    class Meta:
        verbose_name = 'Citizen'

    def __str__(self):
        return self.get_full_name()
