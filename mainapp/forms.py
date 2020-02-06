from django import forms
from mainapp.models import   Song

class AddSong(forms.models.ModelForm):                                        
    class Meta:
        model=Song
        exclude =[]