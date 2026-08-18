from django import forms


class MinistryInterestForm(forms.Form):
    name = forms.CharField(max_length=160)
    email = forms.EmailField()
    ministry = forms.CharField(max_length=160)
    message = forms.CharField(widget=forms.Textarea, required=False)
