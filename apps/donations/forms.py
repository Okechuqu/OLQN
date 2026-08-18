from django import forms


class DonationForm(forms.Form):
    donor_name = forms.CharField(max_length=160, required=False)
    email = forms.EmailField()
    purpose = forms.CharField(max_length=120)
    amount = forms.DecimalField(min_value=100, decimal_places=2)
