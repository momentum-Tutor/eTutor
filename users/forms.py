from django import forms
from django.db import models
from registration.forms import RegistrationForm
from .models import User, Language


class CustomRegistrationForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = User
        fields = RegistrationForm.Meta.fields + ('primary_language', 'known_languages', 'wanted_languages', 'current_time_zone',)

    def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
                self.save_m2m()
            return user
            
class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields=('primary_language', 'known_languages', 'wanted_languages',)
