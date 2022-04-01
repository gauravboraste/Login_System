from dataclasses import field
from pyexpat import model
from django import forms
from .models import Contact
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class EmployeeRegistation(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['id','first_name','last_name','email','username','password']
        help_texts ={
            'username':None,
            'password':None,
        }
    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            raise ValidationError("first name is required.")
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if self.cleaned_data["last_name"].strip() == '':
            raise ValidationError("Last name is required.")
        return self.cleaned_data["last_name"]

    def clean_email(self):
        email = self.cleaned_data['email']
        validator = RegexValidator("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
        validator(email)
        return email

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['name','email','message']
        # widgets = {
        # 'name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
        # 'email':forms.TextInput(attrs={'class':'form-control form-control-user'}) ,
        # 'message':forms.Textarea(attrs={'class':'form-control form-control-user'}) ,
        
        #  }
        # help_texts ={
        #     'name.error':None,
        #     'email':None,
        #     'message':None,
        # }