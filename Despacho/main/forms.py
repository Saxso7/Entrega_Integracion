from django import forms

class Login(forms.Form):
    usuario = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)