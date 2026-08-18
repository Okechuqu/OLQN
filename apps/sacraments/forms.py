from django import forms

from .models import SacramentEnquiry


class SacramentEnquiryForm(forms.ModelForm):
    class Meta:
        model = SacramentEnquiry
        fields = ["sacrament", "name", "email", "message"]
