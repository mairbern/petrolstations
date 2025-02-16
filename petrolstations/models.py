from django.db import models

# Create your models here.

class PetrolStation(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, blank=True)
    diesel_price = models.DecimalField(max_digits=5, decimal_places=3)
    e5_price = models.DecimalField(max_digits=5, decimal_places=3,blank =True)
    e10_price = models.DecimalField(max_digits=5, decimal_places=3)
    electric_fueling = models.BooleanField(default=False)
    last_update = models.DateTimeField("last update")

    def __str__(self):
        return self.name