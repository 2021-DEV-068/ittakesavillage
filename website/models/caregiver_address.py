from django.db import models


class CaregiverAddress(models.Model):
    street = models.CharField(max_length=128)
    street_no = models.CharField(max_length=4)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=64)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.street} {self.street_no}, {self.postal_code} {self.city}"
