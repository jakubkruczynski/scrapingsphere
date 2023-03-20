from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

