from django import forms

class stocks(forms.Form):
    Company_Name=forms.CharField(max_length=200)
    Symbol=forms.CharField(max_length=200)
