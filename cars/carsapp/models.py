from django.db import models


# Create your models here.
class cars(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    year = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    extcolor = models.CharField(max_length=120)
    intcolor = models.CharField(max_length=120)
    transmission = models.CharField(max_length=120)
    price = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)

    def __str__(self):
        return str(self.brand)

    class Meta:
        managed = False
        db_table = 'cars'
