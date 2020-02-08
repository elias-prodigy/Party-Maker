from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    sponsor = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.manager_name}"
