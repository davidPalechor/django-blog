from django import forms
from django.utils import timezone

from .models import Call


class CallCreationForm(forms.ModelForm):
    YEARS = [
        x for x in range(
            timezone.now().year,
            (timezone.now() + timezone.timedelta(days=360 * 5)).year
        )
    ]
    YEAR_CHOICES = [(year, year) for year in YEARS]

    year = forms.ChoiceField(choices=YEAR_CHOICES)
    start_date = forms.DateField()

    class Meta:
        model = Call
        fields = (
            'year',
            'period',
            'start_date',
            'end_date',
        )

    def clean(self):
        if self.cleaned_data['start_date'] > self.cleaned_data['end_date']:
            self.add_error('end_date', 'Invalid call date interval')
