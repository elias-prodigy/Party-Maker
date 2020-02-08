from django.db import models
from django.urls import reverse


class Partners(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    sponsor = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.manager_name}"

    def get_absolute_url_delete(self):
        return reverse('delete_partners', kwargs={'pk': self.pk})

    def get_absolute_url_update(self):
        return reverse('update_partners', kwargs={'pk': self.pk})
