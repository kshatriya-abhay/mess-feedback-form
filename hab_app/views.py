from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from hab_app.models import *
from datetime import *
from django.apps import apps
# Create your views here

def index(request):
    return render(request,'hab_app/login.html')
def details(request):
    return HttpResponse("hello")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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
    start = now - timedelta(hours=24)
    end = now + timedelta(hours=24)
    tobeVacated = mymodel.objects.filter(toRoomStay__range=(start.date(),end.date()))
    return render(request,'hab_app/vacate.html',{'ROtable':ROtable,'tobeVacated':tobeVacated})
def allot(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    return render(request,'hab_app/allot.html',{'ROtable':ROtable})
