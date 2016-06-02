from django import forms
from django.core.validators import validate_email


from .models import Person

class ContactForm(forms.Form):
    member_fname = forms.CharField(required=False)   
    member_email = forms.EmailField()
    message = forms.CharField()

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['person_email', 'person_fname', 'person_lname']

    def clean_email(self):
        email = self.cleaned_data.get('person_email')       
        if not validate_email(email):
            raise forms.ValidationError("Please insert a correct Email")
        return email

    
    def clean_person_fname(self):
        person_fname = self.cleaned_data.get('person_fname')
        return person_fname
    
       
    
   