from django.db import models
from datetime import datetime, date

# Create your models here.
class Operating_system(models.Model):
    operating_system = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.operating_system

class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True, null=True)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now_add = True, auto_now = False, blank=True)
    os_choice = (
            ('Mac OS', 'Mac OS'),
            ('Windows 11', 'Windows 11'),
            ('Windows 10', 'Windows 10'),
            ('Windows 8', 'Windows 8'),
            ('Linux', 'Linux'),
        )
    operating_system = models.CharField(max_length=30, blank=True, null=True, choices=os_choice)

    users_name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField("Purchase mm-dd-yy",auto_now_add = False, auto_now = False, blank=True, null=True)
    
def __unicode__(self):
    return self.users_name + self.IP_address
