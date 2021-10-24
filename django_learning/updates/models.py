from django.db import models
from django.urls import reverse


class OwnerUpdate(models.Model):
    update_title = models.CharField(max_length=100)
    content      = models.TextField()
    update_type  = models.BooleanField(default=False)

    def __str__(self):
        return "Update " + str(self.id)

    def get_absolute_url(self):
        return reverse('updates:update-detail', kwargs={"id": self.id})