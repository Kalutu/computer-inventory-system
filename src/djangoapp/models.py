from django.db import models
from datetime import datetime, date

# Create your models here.
class Operating_system(models.Model):
    operating_system = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.operating_system

class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True, null=True)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now_add = True, auto_now = False, blank=True)
    operating_system = models.ManyToManyField(Operating_system, blank=True)
    users_name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField("Purchase mm-dd-yy",auto_now_add = False, auto_now = False, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
    
    def __str__(self):
        return self.users_name + self.IP_address

class ComputerHistory(models.Model):
    computer_name = models.CharField(max_length=30, blank=True, null=True)
    IP_address = models.CharField(max_length=30, blank=True, null=True)
    MAC_address = models.CharField(max_length=30, blank=True, null=True)
    operating_system = models.ManyToManyField(Operating_system, blank=True)
    users_name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    purchase_date = models.DateField("Purchase Date(mm/dd/2019)", auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.computer_name} ({self.timestamp})"