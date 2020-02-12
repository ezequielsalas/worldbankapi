from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def get_list_name(cls):
        result = Country.objects.values_list("name", flat=True)
        if result:
            return list(result)
        return []

    def __str__(self):
        return "{}".format(self.name)


class Indicator(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    @classmethod
    def get_list_name(cls):
        result = Indicator.objects.values_list("name", flat=True)
        if result:
            return list(result)
        return []

    def __str__(self):
        return "{}".format(self.name)


class CountryData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    indicator = models.ForeignKey(Indicator, on_delete=models.DO_NOTHING)
    value = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    year = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.country, self.year, self.value)


