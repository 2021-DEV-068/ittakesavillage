from django.db import models

from website.models.choices import Speciality


class CaregiverSpeciality(models.Model):
    caregiver = models.ForeignKey('website.Caregiver', on_delete=models.CASCADE, related_name='specialities')
    speciality = models.CharField(max_length=240, choices=Speciality.choices)

    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.caregiver} {self.speciality}"
