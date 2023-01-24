from django.contrib import admin

from website.models.appointment import Appointment
from website.models.caregiver import Caregiver
from website.models.caregiver_address import CaregiverAddress
from website.models.caregiver_consultation_slot import CaregiverConsultationSlot
from website.models.caregiver_diploma import CaregiverDiploma
from website.models.caregiver_speciality import CaregiverSpeciality
from website.models.parent import Parent

admin.site.register(Parent)

admin.site.register(Caregiver)
admin.site.register(CaregiverAddress)
admin.site.register(CaregiverSpeciality)
admin.site.register(CaregiverDiploma)
admin.site.register(CaregiverConsultationSlot)

admin.site.register(Appointment)
