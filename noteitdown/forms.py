from django import forms
from .models import notes
class upload(forms.ModelForm):
    class Meta:
        model = notes
        exclude = ["date_of_pub"]