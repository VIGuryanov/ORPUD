from django import forms

class ObjectForm(forms.Form):
    data = forms.CharField(max_length=256)