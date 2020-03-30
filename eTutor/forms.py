
from django import forms
from .models import Language

class LangaugeForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('name', )