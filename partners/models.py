from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    sponsor = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    manager_approve = models.BooleanField(default = False)
    CEO_approve = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.name} {self.surname} {self.manager_name}"
