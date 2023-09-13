from django.db import models

# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length=30)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    users_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

def __unicode__(self):
    return self.users_name + self.IP_address
