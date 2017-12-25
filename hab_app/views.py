from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from hab_app.models import *
from datetime import *
from django.apps import apps
from hab_app.forms import *
from student_portal.models import *

# Create your views here

def index(request):
    if request.session['username'] == "chr_hab":
        hostels = AllHostelMetaData.objects.all()
        return render(request,'hab_app/chrView.html',{'hostels':hostels})
    elif request.session['username'][-3:]== "off":
        username = request.session['username'][:-3]
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = username)
        return render(request,'hab_app/caretakerView.html',{'ROtable':ROtable})
    elif request.session['username'][:3]== "hod":
        return render(request,'hab_app/headView.html')
    else:
        return render(request,'hab_app/generalView.html')

def login_page(request):
    return render(request,'hab_app/login.html')

@login_required
def logout1(request):
    logout(request)
    return redirect('hab_app:login_page')

def showDetails(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
    if request.method == 'GET':
        parameter = request.GET.get('param')
        details = OccupantDetails.objects.get(idNo = parameter)
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
        temp = ROtable.hostelRoomOccupant
        mymodel = apps.get_model(app_label='hab_app', model_name=temp)
        roDetails = mymodel.objects.get(occupantId__iexact = parameter)
        return render(request,'hab_app/showDetails.html',{'details':details,'roDetails':roDetails})

def showDetails2(request):
    if request.method == 'GET':
        parameter = request.GET.get('param')
        pobj = OccupantDetails.models.get(idNo=parameter)
        details = OccupantDetails.objects.get(idNo = parameter)
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
        temp = ROtable.hostelRoomOccupant
        mymodel = apps.get_model(app_label='hab_app', model_name=temp)
        roDetails = mymodel.objects.get(occupantId__iexact = parameter)
        return render(request,'hab_app/showDetails2.html',{'details':details,'roDetails':roDetails})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                request.session['username'] = username
                request.session['password'] = password
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")
        else:
            return HttpResponse("Invalid Login Credentials")

    else:
        return render(request,'hab_app/login.html')


def home(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
    return render(request,'hab_app/caretakerView.html',{'ROtable':ROtable})


def vacate(request):

    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
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
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
    tobeAlloted = UpcomingOccupant.objects.filter(hostelName__iexact = request.session['username'][:-3])
    # tobeAlloted2 = UpcomingOccupantRequest.objects.filter(hostelName__iexact = request.session['username'][:-3])
    return render(request,'hab_app/allot.html',{'ROtable':ROtable,'tobeAlloted':tobeAlloted})


def chrAllot(request):
    hostels = AllHostelMetaData.objects.all()
    if request.method == 'POST':
        form = UpcomingOccupantForm(data=request.POST)
        if form.is_valid:
            occupant = form.save()
            occupant.save()
            form = UpcomingOccupantForm()
            return render(request,'hab_app/addOccupant.html',{'form':form,'hostels':hostels})
        else:
            print(form.errors)

    else:
        form = UpcomingOccupantForm()
        return render(request,'hab_app/addOccupant.html',{'form':form,'hostels':hostels})

def addDetails(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
    temp = ROtable.hostelRoomOccupant
    mymodel = apps.get_model(app_label='hab_app', model_name=temp)
    if request.method == 'POST':

        form1 = HostelRoomOccupantRelationForm(data=request.POST)
        form2 = OccupantDetailsForm(request.POST, request.FILES)
        if form1.is_valid():
            print("tes")
            occupantId = form1.cleaned_data['occupantId']
            occupant = form1.save(commit=False)
            p = mymodel(occupantId = occupantId)
            p.hostelName = ROtable.hostelName
            p.roomNo = occupant.roomNo
            p.messStatus = occupant.messStatus
            # p.toMess = occupant.toMess
            # p.fromMess = occupant.fromMess
            p.toRoomStay = occupant.toRoomStay
            p.fromRoomStay = occupant.fromRoomStay
            p.comment = occupant.comment
            p.save()


            if form2.is_valid:
                instance = form2.save(commit=False)
                instance.idNo = occupantId
                instance.save()
            else:
                print(form2.errors)
        else:
            print(form1.errors)
        log = UpcomingOccupant.objects.get(occupantId = occupantId).delete()
        tobeAlloted = UpcomingOccupant.objects.filter(hostelName__iexact = request.session['username'][:-3])
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
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
        temp = ROtable.hostelRoomOccupant
        mymodel = apps.get_model(app_label='hab_app', model_name=temp)
        occupantId = request.GET.get('param')
        occupant = mymodel.objects.get(occupantId__iexact=occupantId)
        p = Log_Table(occupantId = occupantId)
        p.hostelName = ROtable.hostelName
        p.roomNo = occupant.roomNo
        p.messStatus = occupant.messStatus
        # p.toMess = occupant.toMess
        # p.fromMess = occupant.fromMess
        p.toRoomStay = occupant.toRoomStay
        p.fromRoomStay = occupant.fromRoomStay
        p.comment = occupant.comment
        p.save()
        occupant = mymodel.objects.get(occupantId=occupantId).delete()
        now = datetime.now()
        start = now - timedelta(days=365)
        end = now + timedelta(days=5)
        tobeVacated = mymodel.objects.filter(toRoomStay__range=(start.date(),end.date()))
        for i in tobeVacated:
            temp1 = OccupantDetails.objects.get(idNo__iexact = i.occupantId)
            i.name = temp1.name
            i.contact = temp1.mobNo
        return render(request,'hab_app/vacate.html',{'ROtable':ROtable,'tobeVacated':tobeVacated})

def existingOccupants(request):
    ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
    temp = ROtable.hostelRoomOccupant
    mymodel = apps.get_model(app_label='hab_app', model_name=temp)
    relation = mymodel.objects.all()
    occupants = list()
    for i in relation:
        if OccupantDetails.objects.filter(idNo__iexact=i.occupantId).count() == 1:
            occupants.append(OccupantDetails.objects.get(idNo__iexact=i.occupantId))
    zipped = zip(relation,occupants)
    return render(request,'hab_app/existingOccupants.html',{'ROtable':ROtable,'zipped':zipped})

def roomDetails(request):
    if request.method == 'GET':
        index = request.GET.get('param')
        #occupied rooms
        #get the relation table name and room table name
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = request.session['username'][:-3])
        relation_table = ROtable.hostelRoomOccupant
        room_table = ROtable.hostelRoom
        # get the model names for query
        relation_model = apps.get_model(app_label='hab_app', model_name=relation_table)
        room_model = apps.get_model(app_label='hab_app', model_name=room_table)
        relation = relation_model.objects.all()
        occupants = list()
        room_list = list()
        for i in relation:
            if OccupantDetails.objects.filter(idNo__iexact=i.occupantId).count() == 1:
                occupants.append(OccupantDetails.objects.get(idNo__iexact=i.occupantId))
                if room_model.objects.filter(roomNo = i.roomNo).count() == 1:
                    room_list.append(room_model.objects.get(roomNo = i.roomNo))

        zipped = zip(room_list,occupants)
        #for empty rooms
        empty_rooms = list()
        all_rooms = room_model.objects.all()
        for i in all_rooms:
            flag = 0
            for j in room_list:
                if i.roomNo == j.roomNo:
                    flag = 1
                    break
            if flag == 0:
                empty_rooms.append(i)
        if index == "1":
            return render(request,'hab_app/occupiedRooms.html',{'ROtable':ROtable,'zipped':zipped})

        elif index == "2":
            #empty rooms
            return render(request,'hab_app/emptyRooms.html',{'ROtable':ROtable,'empty_rooms':empty_rooms})

        else:
            return render(request,'hab_app/totalRooms.html',{'ROtable':ROtable,'zipped':zipped ,'empty_rooms':empty_rooms})



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
        obj = User.objects.get(username = request.session['username'])
        initialData = {'Host_Name':obj.first_name,'Host_Webmail_Id':obj.username}
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
    hostels = AllHostelMetaData.objects.all()
    if request.method == 'GET':
        if request.GET.get('param') :
            idNo = request.GET.get('param')
            guest = UpcomingOccupantRequest.objects.get(id_no = idNo)
            guest.isApprovedChr = "Approved"
            guest.save()
    applicants = UpcomingOccupantRequest.objects.filter( isApprovedFirst = "Approved",isApprovedChr = "Pending" )
    return render(request,"hab_app/chrApproveApplication.html",{'applicants':applicants,'hostels':hostels})


def chrDisapproveApplication(request):
    if request.method == 'GET':
        if request.GET.get('param') :
            idNo = request.GET.get('param')
            guest = UpcomingOccupantRequest.objects.get(id_no = idNo)
            guest.isApprovedChr = "Disapproved"
            guest.save()
    applicants = UpcomingOccupantRequest.objects.filter( isApprovedFirst = "Approved",isApprovedChr = "Pending" )
    return render(request,"hab_app/chrApproveApplication.html",{'applicants':applicants})

def chrViewRoom(request):
    if request.method == 'GET':
        if request.GET.get('param') :
            hostel = request.GET.get('param')
            ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
            relation_table = ROtable.hostelRoomOccupant
            room_table = ROtable.hostelRoom
            # get the model names for query
            relation_model = apps.get_model(app_label='hab_app', model_name=relation_table)
            room_model = apps.get_model(app_label='hab_app', model_name=room_table)
            relation = relation_model.objects.all()
            occupants = list()
            room_list = list()
            for i in relation:
                if OccupantDetails.objects.filter(idNo__iexact=i.occupantId).count() == 1:
                    occupants.append(OccupantDetails.objects.get(idNo__iexact=i.occupantId))
                    if room_model.objects.filter(roomNo = i.roomNo).count() == 1:
                        room_list.append(room_model.objects.get(roomNo = i.roomNo))

            zipped = zip(room_list,occupants)
            #for empty rooms
            empty_rooms = list()
            all_rooms = room_model.objects.all()
            for i in all_rooms:
                flag = 0
                for j in room_list:
                    if i.roomNo == j.roomNo:
                        flag = 1
                        break
                if flag == 0:
                    empty_rooms.append(i)
            hostels = AllHostelMetaData.objects.all()
            return render(request,'hab_app/chrViewRoom.html',{'ROtable':ROtable,'zipped':zipped ,'empty_rooms':empty_rooms,'hostels':hostels})


def chrHostelSummary(request):
    hostels = AllHostelMetaData.objects.all()
    hostel_names = list()

    hostelSummary = list()
    for i in hostels:
        curr_hostel = list()
        hostel = i.hostelName
        ROtable = AllHostelMetaData.objects.get(hostelName__iexact = hostel)
        relation_table = ROtable.hostelRoomOccupant
        room_table = ROtable.hostelRoom
        # get the model names for query
        relation_model = apps.get_model(app_label='hab_app', model_name=relation_table)
        room_model = apps.get_model(app_label='hab_app', model_name=room_table)
        relation = relation_model.objects.all()
        occupants = list()
        room_list = list()

        for i in relation:
            if OccupantDetails.objects.filter(idNo__iexact=i.occupantId).count() == 1:
                occupants.append(OccupantDetails.objects.get(idNo__iexact=i.occupantId))
                if room_model.objects.filter(roomNo = i.roomNo).count() == 1:
                    room_list.append(room_model.objects.get(roomNo = i.roomNo))

        zipped = zip(room_list,occupants)
        #for empty rooms
        empty_rooms = list()
        all_rooms = room_model.objects.all()
        curr_hostel.append(len(all_rooms))
        curr_hostel.append(len(room_list))
        abandoned=0
        usable=0
        partial=0
        # single=0
        # double=0
        # with_toilet=0
        # guest=0
        # official=0
        for i in all_rooms:
            if i.roomStatus == "Abandoned":
                abandoned= abandoned+1
            if i.roomStatus == "Usable":
                usable=usable+1
            if i.roomStatus == "Partially Damaged":
                partial=partial+1
            # if i.roomOccupancyType == RoomCategory.objects.get(roomId=1).description:
            #     print(single)
            #     single=   single+1
            # if i.roomOccupancyType == "Double Occupancy":
            #     double=   double+1
            # if i.roomOccupancyType == "Official Use":
            #     official=   official+1
            # if i.roomOccupancyType == "Guest Room":
            #     guest=   guest+1
            # if i.roomOccupancyType == "Single Occupancy With Toilet":
            #     with_toilet=   with_toilet+1

            flag = 0
            for j in room_list:
                if i.roomNo == j.roomNo:
                    flag = 1
                    break
            if flag == 0:
                empty_rooms.append(i)
        curr_hostel.append(len(empty_rooms))
        curr_hostel.append(usable)
        curr_hostel.append(partial)
        curr_hostel.append(abandoned)
        # curr_hostel.append(single)
        # curr_hostel.append(double)
        # curr_hostel.append(official)
        # curr_hostel.append(guest)
        # curr_hostel.append(with_toilet)
        hostelSummary.append(curr_hostel)
        zipped_summary = zip(hostelSummary,hostels)
    return render(request,'hab_app/chrHostelSummary.html',{'zipped_summary':zipped_summary,'hostels':hostels})

def mess_opi(request):
    opi_calculated_list = Opi_calculated.objects.all()
    print(
    )
    return render(request,'hab_app/opi_student_portal.html', {'opi_calculated_list': opi_calculated_list})

def opi_calculate(request):
    feedbacks = MessFeedback.objects.all()
    print(feedbacks)
    hostelss = []
    noh = 0         # number of hostels
    freq_hostelss = []  #hostel wise freq of the feedback
    for fb in feedbacks:
        #   count No. of feedbacks hostelwise
        if fb.hostelName not in hostelss:
            hostelss.append(fb.hostelName)
            noh = noh + 1
            freq_hostelss.append(1)
        else:
            freq_hostelss[hostelss.index(fb.hostelName)] += 1

#   one loop to calculate sum of 5 fields hostelwise and then take their average
    opis = [0] * len(hostelss)
    for fb in feedbacks:
        opis[hostelss.index(fb.hostelName)] = (fb.cleanliness + fb.qual_b + fb.qual_l + fb.qual_d + fb.catering)/5
    print(opis)
    for fb in feedbacks:
        opis[hostelss.index(fb.hostelName)] = opis[hostelss.index(fb.hostelName)] / freq_hostelss[hostelss.index(fb.hostelName)]
    Opi_calculated.objects.all().delete()
    for i in range(len(opis)):
        opi_object = Opi_calculated(hostelName=hostelss[i])
        opi_object.opi_value = opis[i]
        opi_object.numberOfSubscriptions = freq_hostelss[i]
        opi_object.save()
    return redirect('hab_app:mess_opi')
