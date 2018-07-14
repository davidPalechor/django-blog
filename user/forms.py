from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'confirm_password',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match")

