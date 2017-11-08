from django import forms
from django.contrib.auth.models import User
from hab_app.models import UpcomingOccupant,HostelRoomOccupantRelation,OccupantDetails,UpcomingOccupantRequest

class UpcomingOccupantForm(forms.ModelForm):
    class Meta():
        model = UpcomingOccupant
        fields = ('occupantName','idType','occupantId','hostelName','roomNo','fromStay','toStay')
        toStay = forms.DateField(widget = forms.DateTimeInput())
        fromStay = forms.DateField(widget = forms.DateTimeInput())

class UpcomingOccupantRequestForm(forms.ModelForm):
    class Meta():
        model = UpcomingOccupantRequest
        exclude =('isApprovedChr','isApprovedFirst','hostelName',)
        From_Date = forms.DateField(widget = forms.DateTimeInput())
        To_Date = forms.DateField(widget = forms.DateTimeInput())



class HostelRoomOccupantRelationForm(forms.ModelForm):
    class Meta():
        model = HostelRoomOccupantRelation
        fields = '__all__'
        toMess = forms.DateField(widget = forms.DateTimeInput())
        fromMess = forms.DateField(widget = forms.DateTimeInput())

class OccupantDetailsForm(forms.ModelForm):
    class Meta():
        model = OccupantDetails
        exclude = ('idNo',)
