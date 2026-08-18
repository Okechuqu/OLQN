from django import forms


class EventRegistrationForm(forms.Form):
    name = forms.CharField(max_length=160)
    email = forms.EmailField()
    quantity = forms.IntegerField(min_value=1, max_value=10, initial=1)
