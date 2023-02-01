from decimal import Decimal
from typing import List

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Prefetch

from website.models.caregiver_consultation_slot import CaregiverConsultationSlot
from website.models.choices import Gender, Language


class CaregiverManager(models.Manager):
    def with_consultation_slots(self):
        return self.prefetch_related(
            Prefetch(
                "consultation_slots",
                queryset=CaregiverConsultationSlot.objects.order_by('week_day', 'start'),
                to_attr="available_consultation_slots",
            )
        )


class Caregiver(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.EmailField(max_length=240)

    sex = models.CharField(max_length=1, choices=Gender.choices)
    address = models.OneToOneField(
        'website.CaregiverAddress',
        on_delete=models.PROTECT
    )

    profile_photo = models.ImageField(upload_to="caregivers/profile/")
    profile_video = models.URLField()

    languages = ArrayField(
        models.CharField(max_length=2, choices=Language.choices),
        size=3
    )
    description = models.TextField(max_length=640)

    physical = models.BooleanField(default=True)
    online = models.BooleanField(default=False)
    conditions = ArrayField(
        models.CharField(max_length=128),
        size=5,
    )

    ranking = models.FloatField()
    number_comments = models.PositiveIntegerField()

    objects = CaregiverManager()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def min_rate(self) -> Decimal:
        specialities = self.specialities.all()
        return min((speciality.rate for speciality in specialities), default=Decimal(0))

    @property
    def max_rate(self) -> Decimal:
        specialities = self.specialities.all()
        return max((speciality.rate for speciality in specialities), default=Decimal(0))

    @property
    def languages_names(self) -> List[str]:
        return [value for label, value in Language.choices if label in self.languages]
