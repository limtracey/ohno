from django import forms

class CreateThought(forms.Form):
    thought = forms.CharField(label="Thought",max_length=200)
