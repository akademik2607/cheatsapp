from django import forms

from cheats.models import Category


class CheatForm(forms.Form):
    category = forms.SlugField()
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField()
