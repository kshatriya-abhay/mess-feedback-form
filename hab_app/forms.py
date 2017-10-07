from django import forms
from django.contrib.auth.models import User
from hab_app.models import UpcomingOccupant,HostelRoomOccupantRelation,OccupantDetails

class UpcomingOccupantForm(forms.ModelForm):
    class Meta():
        model = UpcomingOccupant
        fields = ('occupantName','occupantIdCategory','occupantId','hostelName','roomNo','fromStay','toStay')
# class HostelRoomOccupantRelationForm(forms.ModelForm):
#     class Meta():
#         model = HostelRoomOccupantRelation
# class OccupantDetailsForm(forms.ModelForm):
#     class Meta():
#         model =
