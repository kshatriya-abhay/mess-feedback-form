from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from hab_app.models import *
from datetime import *
from django.apps import apps
from hab_app.forms import UpcomingOccupantForm
# Create your views here

def index(request):
    return render(request,'hab_app/login.html')



def showDetails(request):
    if request.method == 'GET':
        parameter = request.GET.get('param')
        details = OccupantDetails.objects.get(idNo = parameter)
        return render(request,'hab_app/showDetails.html',{'details':details})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        if username == "chr_hab":
            return render(request,'hab_app/chrView.html')

        else:
            username = username[:-3]
            global hostel
            hostel = username
            ROtable = AllHostelMetaData.objects.get(hostelName__iexact = username)
            return render(request,'hab_app/caretakerView.html',{'ROtable':ROtable})
    else:
        return render(request,'hab_app/login.html')


def home(request):
    return render(request,'hab_app/caretakerView.html')


def vacate(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    temp = ROtable.hostelRoomOccupant
    mymodel = apps.get_model(app_label='hab_app', model_name=temp)
    now = datetime.now()
    start = now - timedelta(days=1)
    end = now + timedelta(days=1)
    tobeVacated = mymodel.objects.filter(toRoomStay__range=(start.date(),end.date()))
    for i in tobeVacated:
        temp1 = OccupantDetails.objects.get(idNo__iexact = i.occupantId)
        i.name = temp1.name
        i.contact = temp1.mobNo
    return render(request,'hab_app/vacate.html',{'ROtable':ROtable,'tobeVacated':tobeVacated})


def allot(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    return render(request,'hab_app/allot.html',{'ROtable':ROtable})



def chrAllot(request):
    if request.method == 'POST':
        form = UpcomingOccupantForm(data=request.POST)
        if form.is_valid:
            occupant = form.save()
            occupant.save()
            form = UpcomingOccupantForm()
            return render(request,'hab_app/addOccupant.html',{'form':form})
        else:
            print(form.errors)

    else:
        form = UpcomingOccupantForm()
        return render(request,'hab_app/addOccupant.html',{'form':form})
