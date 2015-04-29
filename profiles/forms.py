from django import forms
from .models import Profile

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=120, required=True) #set required to False if user does not need to input
    last_name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField()
    
class ProfileForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email"]
