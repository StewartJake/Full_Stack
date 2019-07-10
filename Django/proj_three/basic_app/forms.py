from django import forms
from django.core import validators

#def check_for_z(value):
#    if value[0].lower() != 'z':
#        raise forms.ValidationError('NAME MUST BEGIN WITH "Z"')


class norm_form(forms.Form):
#    name = forms.CharField(validators=[check_for_z]v)
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify email.")
    text = forms.CharField(widget=forms.Textarea)
#    bot_catcher = forms.CharField(required=False,
#                                widget=forms.HiddenInput,
#                                validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError("Emails don't match")




