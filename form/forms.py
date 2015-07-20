from django import forms
from form.models import FarmDescription

class NewFarmForm(forms.ModelForm):
    class Meta:
        model = FarmDescription
        exclude = ["owner"]