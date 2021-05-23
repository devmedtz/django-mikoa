from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=200, unique=True)
    capital = models.CharField(max_length=200, unique=True, blank=True, null=True)
    districts = models.PositiveIntegerField(blank=True, null=True)
    postcode = models.CharField(max_length=50, unique=True, blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    population = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)