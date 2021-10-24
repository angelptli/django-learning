from django.db import models
from django.urls import reverse


class DimSumItem(models.Model):
    item_name    = models.CharField(max_length=100)
    description  = models.TextField(null=True, blank=True)
    normal_price = models.DecimalField(decimal_places=2, max_digits=1000)
    history      = models.TextField(null=True, blank=True)
    tasty        = models.BooleanField(default=True)

    def __str__(self):
        return str.title(self.item_name)

    def get_absolute_url(self):
        # return f"/dimsum/{self.id}/"
        return reverse("dim_sum_detail", kwargs={"id": self.id})