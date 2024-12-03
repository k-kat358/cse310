from django import forms
from .models import Guides, GuidesImages

class GuidesForm(forms.ModelForm):
    class Meta:
        model = Guides
        fields = '__all__'

class GuidesImagesForm(forms.ModelForm):
    class Meta:
        model = GuidesImages
        fields = '__all__'
