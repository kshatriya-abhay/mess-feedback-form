from django.db import models


#table with general information regarding all hostels
class AllHostelMetaData(models.Model):

    class Meta:
        verbose_name = "AllHostelMetaData"
        verbose_name_plural = "AllHostelMetaData"

    hostelName = models.CharField(max_length=255,primary_key=True)
    hostelCode = models.CharField(max_length=255,unique=True)
    #gensec webmail id
    hostelGensec = models.CharField(max_length=255,null=False)
    #caretaker office id
    hostelCTid = models.CharField(max_length=255,unique=True)
    #hostel rooms table name
    hostelRoom = models.CharField(max_length=255,unique=True)
    #room occupant relation table name
    hostelRoomOccupant = models.CharField(max_length=255,unique=True)
    #view permission table name
    hostelViewPermission = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.hostelName

#table with different room categories and its abbrevations used

class RoomCategory(models.Model):
    class Meta:
        verbose_name = "RoomCategory"
        verbose_name_plural = "RoomCategory"

    roomId = models.IntegerField(null=False)
    abbrevation = models.CharField(max_length=255,primary_key=True)
    #description such as single occupancy/double occupancy/attached toilets etc
    description = models.CharField(max_length=255,null=False)

#table with different occupant categories and its abbrevations used

class OccupantCategory(models.Model):
    class Meta:
        verbose_name = "OccupantCategory"
        verbose_name_plural = "OccupantCategory"
    occupantId = models.IntegerField(null=False)
    abbrevation = models.CharField(max_length=255,primary_key=True)
    #description - student/project staff etc
    description = models.CharField(max_length=255,null=False)

#table with details of rooms in hostels .one for each hostel

class HostelRoom(models.Model):
    class Meta:
        verbose_name = "HostelRoom"
        verbose_name_plural = "HostelRoom"
    roomNo = models.CharField(max_length=255,primary_key=True)
    #occupancy as singlee/double etc
    roomOccupancyType = models.CharField(max_length=255,null=False)
    #floor as 1st/2nd etc
    floorInfo = models.CharField(max_length=255)
    #status as abandoned/partially damaged etc
    roomStatus = models.CharField(max_length=255)
    roomOccupancyGender = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)

#table with information regarding occupants staying in hostel.one for each hostel

class HostelRoomOccupantRelation(models.Model):
    class Meta:
        verbose_name = "HostelRoomOccupantRelation"
        verbose_name_plural = "HostelRoomOccupantRelation"
    hostelName = models.CharField(max_length=255)
    roomNo = models.CharField(max_length=255)
    occupantId = models.CharField(max_length=255)
    #mess subscription status
    messStatus = models.CharField(max_length=255)
    #toMess - end date of mess subscription
    toMess = models.DateField()
    #fromMess - start date of mess subscription
    fromMess = models.DateField()
    #toRoomStay - end date of room stay
    toRoomStay = models.DateField()
    #fromRoomStay - start date of room stay
    fromRoomStay = models.DateField()
    comment = models.CharField(max_length=255)

#table with name and webmail of the people with access permissions(view only).one for each hostel

class HostelViewAccess(models.Model):
    class Meta:
        verbose_name = "HostelViewAccess"
        verbose_name_plural = "HostelViewAccess"
    name = models.CharField(max_length=255,null=False)
    webmail = models.CharField(max_length=255,primary_key=True)


#table with all information of a particular OccupantDetails

class OccupantDetails(models.Model):

    class Meta:
        verbose_name = "OccupantDetails"
        verbose_name_plural = "OccupantDetails"
    #id type - roll no/aadhar no/project id etc
    idType = models.CharField(max_length=255)
    #rollno/aadhar no etc
    idNo = models.CharField(max_length=255,primary_key=True)
    gender = models.CharField(max_length=255)
    #specially abled/differently abled
    saORda = models.CharField(max_length=255)
    webmail = models.CharField(max_length=255)
    altEmail = models.CharField(max_length=255,null=False)
    mobNo = models.CharField(max_length=255,null=False)
    emgercencyNo = models.CharField(max_length=255,null=False)
    photo = models.ImageField(upload_to='profile_pics',blank=True)

    bankAccount = models.CharField(max_length=255)
    IFSCCode = models.CharField(max_length=255)
    #account holder name
    accHolderName = models.CharField(max_length=255)

#following are the hostelRoom,roomOccupantRelation and view access tables for each hostel(13*3=39 tables)
#hostelRoom inherits HostelRoom
#hostelView inherits HostelViewAccess
#hostelRORelation inherits HostelRoomOccupantRelation

class siangRoom(HostelRoom):
    pass
class siangView(HostelViewAccess):
    pass
class siangRORelation(HostelRoomOccupantRelation):
    pass

class lohitRoom(HostelRoom):
    pass
class lohitView(HostelViewAccess):
    pass
class lohitRORelation(HostelRoomOccupantRelation):
    pass

class dihingRoom(HostelRoom):
    pass
class dihingView(HostelViewAccess):
    pass
class dihingRORelation(HostelRoomOccupantRelation):
    pass

class dibangRoom(HostelRoom):
    pass
class dibangView(HostelViewAccess):
    pass
class dibangRORelation(HostelRoomOccupantRelation):
    pass

class kapiliRoom(HostelRoom):
    pass
class kapiliView(HostelViewAccess):
    pass
class kapiliRORelation(HostelRoomOccupantRelation):
    pass

class manasRoom(HostelRoom):
    pass
class manasView(HostelViewAccess):
    pass
class manasRORelation(HostelRoomOccupantRelation):
    pass

class barakRoom(HostelRoom):
    pass
class barakView(HostelViewAccess):
    pass
class barakRORelation(HostelRoomOccupantRelation):
    pass

class umiamRoom(HostelRoom):
    pass
class umiamView(HostelViewAccess):
    pass
class umiamRORelation(HostelRoomOccupantRelation):
    pass

class bramhaputraRoom(HostelRoom):
    pass
class bramhaputraView(HostelViewAccess):
    pass
class bramhaputraRORelation(HostelRoomOccupantRelation):
    pass

class dhansiriRoom(HostelRoom):
    pass
class dhansiriView(HostelViewAccess):
    pass
class dhansiriRORelation(HostelRoomOccupantRelation):
    pass

class subansiriRoom(HostelRoom):
    pass
class subansiriView(HostelViewAccess):
    pass
class subansiriRORelation(HostelRoomOccupantRelation):
    pass

class kamengRoom(HostelRoom):
    pass
class kamengView(HostelViewAccess):
    pass
class kamengRORelation(HostelRoomOccupantRelation):
    pass

class marriedScholarRoom(HostelRoom):
    pass
class marriedScholarView(HostelViewAccess):
    pass
class marriedScholarRORelation(HostelRoomOccupantRelation):
    pass
