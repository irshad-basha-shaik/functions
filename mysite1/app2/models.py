from datetime import date

from django.db import models

class SettingModel(models.Model):
    receive_newsletter = models.BooleanField()
    days = models.IntegerField(default=31)
    sex = models.CharField(max_length=100)
    dob = models.DateField(default=date(1111, 11, 11))
