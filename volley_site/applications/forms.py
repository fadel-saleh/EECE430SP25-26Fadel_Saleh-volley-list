from django import forms
from .models import player

class playerForm(forms.ModelForm):
    class Meta:
        model = player
        fields = ['id', 'name', 'date_joined', 'position', 'salary', 'contact_person']