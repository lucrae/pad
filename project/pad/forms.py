from django import forms

class EntryForm(forms.Form):
    body = forms.CharField()