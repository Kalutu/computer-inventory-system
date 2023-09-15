from django.db import models
from datetime import datetime, date

# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True, null=True)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    users_name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField("Purchase mm-dd-yy",auto_now_add = False, auto_now = False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add = True, auto_now = False, blank=True)


def __unicode__(self):
    return self.users_name + self.IP_address
