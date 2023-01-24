import datetime
import itertools
from typing import Iterable

from django import template

from website.models.caregiver_consultation_slot import CaregiverConsultationSlot

register = template.Library()


@register.inclusion_tag('website/parent/blocks/appointment_calendar.html')
def show_appointment_calendar(consultation_slots: Iterable['CaregiverConsultationSlot'], limit=4):
    days = [datetime.date.today() + datetime.timedelta(days=i) for i in range(0, 7)]
    slots_by_day = _get_slots_by_day(days, list(consultation_slots.all()))
    slots = itertools.zip_longest(*slots_by_day, fillvalue=None)
    return {
        'days': days,
        'slots': list(slots),
        'limit': limit
    }


def _get_slots_by_day(days: Iterable['datetime.date'], slots):
    result = []
    slots_grouped_by_weekday = itertools.groupby(slots, key=lambda slot: slot.numeric_iso_week_day())
    slots_grouped_by_weekday = {week_day: list(slots) for week_day, slots in slots_grouped_by_weekday}
    for day in days:
        result.append(slots_grouped_by_weekday.get(day.isoweekday(), list()))

    return result



