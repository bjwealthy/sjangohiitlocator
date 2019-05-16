from django.db import models

# Create your models here.


class Location(models.Model):
    foruser = models.CharField(max_length=30)
    Ipaddress = models.TextField()
    def __str__(self):
        return self.foruser
