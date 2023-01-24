from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, CharFilter, BooleanFilter, ChoiceFilter, MultipleChoiceFilter

from website.models.caregiver import Caregiver
from website.models.choices import Language, Speciality, City


class CaregiverFilter(FilterSet):
    location = CharFilter(field_name='address__city', lookup_expr='icontains', label=_('Location'))
    speciality = ChoiceFilter(
        choices=Speciality.choices,
        method='filter_by_speciality',
        label=_('Speciality'),
    )
    language = MultipleChoiceFilter(
        choices=Language.choices,
        method='filter_by_language',
        label=_('Language'),
        widget=forms.SelectMultiple(attrs={"data-placeholder": _('Language')})
    )
    appointments = MultipleChoiceFilter(
        choices=(('physical', _('physical')), ('online', _('online'))),
        method='filter_by_appointments',
        label=_('Appointments'),
        widget=forms.SelectMultiple(attrs={"data-placeholder": _('Appointments')})
    )
    city = ChoiceFilter(
        choices=City.choices,
        method='filter_by_city',
        label=_('City'),
    )

    class Meta:
        model = Caregiver
        fields = [
            'physical',
            'online',
            'sex'
        ]
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.BooleanField: {
                'filter_class': BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
        }

    def filter_by_language(self, queryset, name, value):
        return queryset.filter(languages__contains=[value])

    def filter_by_speciality(self, queryset, name, value):
        return queryset.filter(specialities__speciality=value)

    def filter_by_city(self, queryset, name, value):
        return queryset.filter(address__city=value)

    def filter_by_appointments(self, queryset, name, value):
        return queryset
