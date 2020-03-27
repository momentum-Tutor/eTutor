# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class SignUpForm(UserCreationForm):
#     name = forms.CharField(max_length=100, help_text='Last Name')
#     email = forms.EmailField(max_length=150, help_text='Email')


#     class Meta:
#         model = User
#         fields = ('username', 'name',
# 'email', 'password1', 'password2',)

from django import forms
from .models import Language

class LangaugeForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('name', )