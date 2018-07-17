from django import forms
from .models import PersonUser


class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = PersonUser
        fields = [
            'id_type',
            'id',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')
