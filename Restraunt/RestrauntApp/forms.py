from django import forms
from .models import table_booking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = table_booking
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "guests",
            "table_size",
            "table_number",
            "date",
            "time"
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }
