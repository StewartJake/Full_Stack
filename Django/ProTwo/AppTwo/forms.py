from django import forms
from AppTwo.models import User


class User_Form(forms.ModelForm):
    class Meta():
        model = User
        fields= '__all__'
        
