from django.db import models

class DimSumItem(models.Model):
    item_name    = models.CharField(max_length=100)
    description  = models.TextField(null=True, blank=True)
    normal_price = models.DecimalField(decimal_places=2, max_digits=1000)
    history      = models.TextField(null=True, blank=True)
    # Set default to True from makemigrations on the command line.
    # This sets existing objects to have this default value.
    # tasty        = models.BooleanField()

    def __str__(self):
        return str.title(self.item_name)