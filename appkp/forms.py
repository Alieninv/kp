from django.forms import ModelForm, forms
from .models import *


class PersonForm(ModelForm):
    class Meta:
        model=Personn
        fields='__all__'
    def clean(self):
        name1=self.cleaned_data['name']
        if len(name1)<4:
            raise forms.ValidationError('name should have atleast 4 charecters')