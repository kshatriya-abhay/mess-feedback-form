from django import forms
from django.contrib.auth.models import User
from hab_app.models import UpcomingOccupant

class UpcomingOccupantForm(forms.ModelForm):
    class Meta():
        model = UpcomingOccupant
        fields = ('occupantName','occupantIdCategory','occupantId','hostelName','roomNo','fromStay','toStay')
