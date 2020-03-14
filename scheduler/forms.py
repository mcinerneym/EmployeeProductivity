from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ShiftForm(forms.Form):
    STATUS = (
        ("H", "Present"),
        ("C", "Call Off"),
        ("N", "No Call No Show"),
        ("L", "Late"),
        ("E", "Left Early"),
        ("M", "Medical"),
        ("Z", "Not Here Yet"),
    )
    start_time = forms.TimeField(label='Start Time')
    end_time = forms.TimeField(label='End Time')
    date = forms.DateField(label = 'Date')
    status = forms.CharField(label = 'Status', max_length=1, choices=STATUS, default="Z")
    reason = forms.CharField(label = 'Reason', max_length=64, blank=True)