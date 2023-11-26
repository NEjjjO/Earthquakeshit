# forms.py
from django import forms

class EventForm(forms.Form):
    start_time = forms.DateTimeField(label='Start Time')
    end_time = forms.DateTimeField(label='End Time')
    magnitude = forms.FloatField(label='Magnitude', min_value=0, max_value=10)
    depth = forms.FloatField(label='Depth', min_value=0)
    latitude = forms.FloatField(label='Latitude', min_value=43, max_value=48.5)
    longitude = forms.FloatField(label='Longitude', min_value=20, max_value=30)
