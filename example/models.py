from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    region = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.name)
