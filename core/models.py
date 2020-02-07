from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)


class CountryEconomy(models.Model):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.country, self.year, self.value)


