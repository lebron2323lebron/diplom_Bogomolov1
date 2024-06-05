from django import forms
from phonenumber_field.formfields import PhoneNumberField

from main.models import ParticipationApplication, Course


class ApplicationForm(forms.ModelForm):
    phone_number = PhoneNumberField()
    course = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = ParticipationApplication
        fields = ("course", "phone_number", "price", "date", "time", "wishes")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"})
        }
