from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=[ 'Area','Bedrooms','Bathrooms','Floors','YearBuilt','Location','Condition','Garage','Location_ratio']
