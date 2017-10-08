from django import forms
from django.contrib.auth.models import User
from hab_app.models import UpcomingOccupant,HostelRoomOccupantRelation,OccupantDetails
from django.contrib.admin.widgets import AdminDateWidget
class UpcomingOccupantForm(forms.ModelForm):
    class Meta():
        model = UpcomingOccupant
        fields = ('occupantName','idType','occupantId','hostelName','roomNo','fromStay','toStay')
        model.toStay = forms.DateField(widget = AdminDateWidget )
        model.fromStay = forms.DateField(widget = AdminDateWidget )


class HostelRoomOccupantRelationForm(forms.ModelForm):
    class Meta():
        model = HostelRoomOccupantRelation
        fields = '__all__'

class OccupantDetailsForm(forms.ModelForm):
    class Meta():
        model = OccupantDetails
        exclude = ('idNo',)
