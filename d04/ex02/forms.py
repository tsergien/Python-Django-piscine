from django import forms

class SimpleForm(forms.Form):
    content = forms.CharField(label='Enter something', max_length=100)
