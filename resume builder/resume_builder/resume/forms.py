from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class createuser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'Repeat password'})
