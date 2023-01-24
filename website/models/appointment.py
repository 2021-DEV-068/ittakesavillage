import datetime
from typing import Tuple

from django.db import models


class Appointment(models.Model):
    specialist = models.ForeignKey("website.Caregiver", on_delete=models.PROTECT)
    parent = models.ForeignKey("website.Parent", on_delete=models.PROTECT)

    start = models.DateTimeField()
    end = models.DateTimeField()

    booked_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.parent}   {self.start} - {self.end}"
