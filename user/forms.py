from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import PersonUser


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
    )
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href='../password/'>this form</a>."
    )

    class Meta:
        model = PersonUser
        fields = [
            'first_name',
            'last_name',
            'password',
            'is_active',
            'is_superuser',
        ]

    def clean_password(self):
        return self.initial['password']
