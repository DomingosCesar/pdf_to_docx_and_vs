from django import forms
from . import models

class FilesForm(forms.ModelForm):
    class Meta:
        model = models.ConvertedFiles
        fields = ['input_path']