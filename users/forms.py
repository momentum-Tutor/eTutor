from django import forms
from registration.forms import RegistrationForm
from .models import User

class CustomRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
       

    class Meta(RegistrationForm.Meta):
        model = User
        fields = fields = ['username', 'first_name', 'last_name', 'email']