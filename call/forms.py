from django import forms

from .models import Call


class CallCretionForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = (
            'year',
            'period',
            'start_date',
            'end_date',
        )

    def clean(self):
        if self.cleaned_data['start_date'] < self.cleaned_data['end_date']:
            self.add_error('end_date', 'Invalid call date interval')
