from django.db import models
from django.utils.translation import gettext_lazy as _


class Sex(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')
    OTHER = 'O', _('Other')


class Language(models.TextChoices):
    FRENCH = 'FR', _('French')
    ENGLISH = 'EN', _('English')
    DUTCH = 'NL', _('Dutch')
    PORTUGUESE = 'PT', _('Portuguese')


class Speciality(models.TextChoices):
    LACTATION = 'Certified Breastfeeding Specialist', _('Certified Breastfeeding Specialist'),
    HYPNO_BIRTHING = 'HypnoBirthing® Childbirth Educator', _('HypnoBirthing® Childbirth Educator')
    MIDWIFE = 'Midwife', _('Midwife')
    DOULA = 'Doula', _('Doula')
    LACTATION_BREASTFEEDING_CONSULTANT = 'Lactation/breastfeeding consultant', _('Lactation/breastfeeding consultant')
    BABYWEARING_SPECIALIST = 'Babywearing specialist', _('Babywearing specialist')
    SLEEP_SPECIALIST = 'Sleep specialist', _('Sleep specialist')
    PEDIATRICIAN = 'Pediatrician', _('Pediatrician')
    PERINATAL_PSYCHOLOGIST = 'Perinatal psychologist', _('Perinatal psychologist')
    PHYSICAL_THERAPIST = 'Physical therapist', _('Physical therapist')
    PRE_POST_NATAL_YOGA_TEACHER = 'Pre/post natal yoga teacher', _('Pre/post natal yoga teacher')
    PRE_POST_NATAL_MASSAGE = 'Pre/post natal massage', _('Pre/post natal massage')
    BABY_MASSAGE = 'Baby massage', _('Baby massage')
    PRE_POST_NATAL_PHYSICAL_THERAPIST = 'Pre/post natal physical therapist', _('Pre/post natal physical therapist')
    OSTEOPATH = 'Osteopath', _('Osteopath')
    PARENTING_COACH = 'Parenting coach', _('Parenting coach')
    PSYCHOMOTRICIAN = 'Psychomotrician', _('Psychomotrician')

    @classmethod
    def availability_choices(cls):
        return [
            (cls.LACTATION.name, cls.LACTATION.label),
            (cls.HYPNO_BIRTHING.name, cls.HYPNO_BIRTHING.label)
        ]


class City(models.TextChoices):
    BRUSSELS = 'Brussels', _('Brussels')
    ANTWERPEN = 'Antwerpen', _('Antwerpen')
    GHENT = 'Ghent', _('Ghent')


class WeekDays(models.TextChoices):
    MONDAY = "Monday", _("Monday")
    TUESDAY = "Tuesday", _("Tuesday")
    WEDNESDAY = "Wednesday", _("Wednesday")
    THURSDAY = "Thursday", _("Thursday")
    FRIDAY = "Friday", _("Friday")
    SATURDAY = "Saturday", _("Saturday")
    SUNDAY = "Sunday", _("Sunday")
