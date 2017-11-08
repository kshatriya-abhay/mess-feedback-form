from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from hab_app.models import *
from datetime import *
from django.apps import apps
from hab_app.forms import *
# Create your views here

def index(request):
    return render(request,'hab_app/login.html')


def showDetails(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    if request.method == 'GET':
        parameter = request.GET.get('param')
        details = OccupantDetails.objects.get(idNo = parameter)
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
        temp = ROtable.hostelRoomOccupant
        mymodel = apps.get_model(app_label='hab_app', model_name=temp)
        roDetails = mymodel.objects.get(occupantId__iexact = parameter)
        return render(request,'hab_app/showDetails.html',{'details':details,'roDetails':roDetails})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        request.session['password'] = password
        if Login.objects.filter(webmail=username).count() == 1:

            if username == "chr_hab":
                return render(request,'hab_app/chrView.html')

            elif username[-3:]== "off":
                username = username[:-3]
                global hostel
                hostel = username
                ROtable = AllHostelMetaData.objects.get(hostelName__iexact = username)
                return render(request,'hab_app/caretakerView.html',{'ROtable':ROtable})
            elif username[:3]== "hod":
                return render(request,'hab_app/headView.html')
            else:
                return render(request,'hab_app/generalView.html')

        else:
            return render(request,'hab_app/login.html')


def home(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    return render(request,'hab_app/caretakerView.html',{'ROtable':ROtable})


def vacate(request):

    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    temp = ROtable.hostelRoomOccupant
    mymodel = apps.get_model(app_label='hab_app', model_name=temp)
    now = datetime.now()
    start = now - timedelta(days=4)
    end = now + timedelta(days=4)
    tobeVacated = mymodel.objects.filter(toRoomStay__range=(start.date(),end.date()))
    for i in tobeVacated:
        temp1 = OccupantDetails.objects.get(idNo__iexact = i.occupantId)
        i.name = temp1.name
        i.contact = temp1.mobNo
    return render(request,'hab_app/vacate.html',{'ROtable':ROtable,'tobeVacated':tobeVacated})


def allot(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    tobeAlloted = UpcomingOccupant.objects.filter(hostelName__iexact = hostel)
    # tobeAlloted2 = UpcomingOccupantRequest.objects.filter(hostelName__iexact = hostel)
    return render(request,'hab_app/allot.html',{'ROtable':ROtable,'tobeAlloted':tobeAlloted})



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

def addDetails(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
    temp = ROtable.hostelRoomOccupant
    mymodel = apps.get_model(app_label='hab_app', model_name=temp)
    if request.method == 'POST':
        form1 = HostelRoomOccupantRelationForm(data=request.POST)
        form2 = OccupantDetailsForm(data=request.POST)

        if form1.is_valid():
            occupantId = form1.cleaned_data['occupantId']
            occupant = form1.save(commit=False)
            p = mymodel(occupantId = occupantId)
            p.hostelName = ROtable.hostelName
            p.roomNo = occupant.roomNo
            p.messStatus = occupant.messStatus
            p.toMess = occupant.toMess
            p.fromMess = occupant.fromMess
            p.toRoomStay = occupant.toRoomStay
            p.fromRoomStay = occupant.fromRoomStay
            p.comment = occupant.comment
            p.save()


            if form2.is_valid:
                instance = form2.save(commit=False)
                instance.idNo = occupantId
                instance.save()
        log = UpcomingOccupant.objects.get(occupantId = occupantId).delete()
        tobeAlloted = UpcomingOccupant.objects.all()
        return render(request,'hab_app/allot.html',{'ROtable':ROtable,'tobeAlloted':tobeAlloted})

    if request.method == 'GET':
        occupantId = request.GET.get('param')
        tobeAlloted = UpcomingOccupant.objects.get(occupantId = occupantId)
        initialData1 = {'occupantId': tobeAlloted.occupantId,'hostelName': tobeAlloted.hostelName,'roomNo': tobeAlloted.roomNo,'fromRoomStay': tobeAlloted.fromStay,'toRoomStay': tobeAlloted.toStay}
        initialData2 = {'name':tobeAlloted.occupantName,'idType':tobeAlloted.idType}
        form1 = HostelRoomOccupantRelationForm(initial = initialData1)
        form2 = OccupantDetailsForm(initial = initialData2)
        return render(request,'hab_app/temp.html',{'form1':form1,'form2':form2})
def deleteDetails(request):
    if request.method == 'GET':
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
        temp = ROtable.hostelRoomOccupant
        mymodel = apps.get_model(app_label='hab_app', model_name=temp)
        occupantId = request.GET.get('param')
        occupant = mymodel.objects.get(occupantId__iexact=occupantId)
        p = Log_Table(occupantId = occupantId)
        p.hostelName = ROtable.hostelName
        p.roomNo = occupant.roomNo
        p.messStatus = occupant.messStatus
        p.toMess = occupant.toMess
        p.fromMess = occupant.fromMess
        p.toRoomStay = occupant.toRoomStay
        p.fromRoomStay = occupant.fromRoomStay
        p.comment = occupant.comment
        p.save()
        occupant = mymodel.objects.get(occupantId=occupantId).delete()
        now = datetime.now()
        start = now - timedelta(days=8)
        end = now + timedelta(days=8)
        tobeVacated = mymodel.objects.filter(toRoomStay__range=(start.date(),end.date()))
        for i in tobeVacated:
            temp1 = OccupantDetails.objects.get(idNo__iexact = i.occupantId)
            i.name = temp1.name
            i.contact = temp1.mobNo
        return render(request,'hab_app/vacate.html',{'ROtable':ROtable,'tobeVacated':tobeVacated})


def generalAllot(request):
    if request.method == 'POST':
        form = UpcomingOccupantRequestForm(data=request.POST)
        if form.is_valid():
            occupant = form.save()
            occupant.save()
            obj = Login.objects.get(webmail = request.session['username'])
            initialData = {'Host_Name':obj.name,'Host_Webmail_Id':obj.webmail}
            form1 = UpcomingOccupantRequestForm(initial = initialData)
            return render(request,'hab_app/generalAllot.html',{'form':form1})
        else:
            print(form.errors)
    else:
        obj = Login.objects.get(webmail = request.session['username'])
        initialData = {'Host_Name':obj.name,'Host_Webmail_Id':obj.webmail}
        form = UpcomingOccupantRequestForm(initial = initialData)
        return render(request,"hab_app/generalAllot.html",{'form':form})


def trackApplication(request):
    applicants = UpcomingOccupantRequest.objects.filter(Host_Webmail_Id = request.session['username'])
    return render(request,"hab_app/generalTrack.html",{'applicants':applicants})

def approveApplication(request):
    if request.method == 'GET':
        if request.GET.get('param') :
            idNo = request.GET.get('param')
            guest = UpcomingOccupantRequest.objects.get(id_no = idNo)
            guest.isApprovedFirst = "Approved"
            guest.save()
    applicants = UpcomingOccupantRequest.objects.filter(To_be_approved_by__iexact = request.session['username'] , isApprovedFirst = "Pending" )
    return render(request,"hab_app/approveApplication.html",{'applicants':applicants})


def disapproveApplication(request):
    if request.method == 'GET':
        if request.GET.get('param') :
            idNo = request.GET.get('param')
            guest = UpcomingOccupantRequest.objects.get(id_no = idNo)
            guest.isApprovedFirst = "Disapproved"
            guest.save()
    applicants = UpcomingOccupantRequest.objects.filter(To_be_approved_by__iexact = request.session['username'] , isApprovedFirst = "Pending" )
    return render(request,"hab_app/approveApplication.html",{'applicants':applicants})

def chrApproveApplication(request):
    if request.method == 'GET':
        if request.GET.get('param') :
            idNo = request.GET.get('param')
            guest = UpcomingOccupantRequest.objects.get(id_no = idNo)
            guest.isApprovedChr = "Approved"
            guest.save()
    applicants = UpcomingOccupantRequest.objects.filter( isApprovedFirst = "Approved",isApprovedChr = "Pending" )
    return render(request,"hab_app/chrApproveApplication.html",{'applicants':applicants})


def chrDisapproveApplication(request):
    if request.method == 'GET':
        if request.GET.get('param') :
            idNo = request.GET.get('param')
            guest = UpcomingOccupantRequest.objects.get(id_no = idNo)
            guest.isApprovedChr = "Disapproved"
            guest.save()
    applicants = UpcomingOccupantRequest.objects.filter( isApprovedFirst = "Approved",isApprovedChr = "Pending" )
    return render(request,"hab_app/chrApproveApplication.html",{'applicants':applicants})
