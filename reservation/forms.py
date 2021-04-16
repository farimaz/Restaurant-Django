from django import forms
from . import models
class ResevationForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = "__all__"