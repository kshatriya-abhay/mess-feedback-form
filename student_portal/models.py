from django.db import models
from datetime import datetime
curr_month = datetime.now().month
curr_year = datetime.now().year
m1 = curr_month
y1 = curr_year
m1 = m1 - 1
m1_y1 = ""
if m1 < 1:
    m1 = 12
    y1 = y1 - 1
m1_y1 = str(m1) + '_' + str(y1)


m2 = curr_month
y2 = curr_year
m2 = m2 + 1
m2_y2 = ""
if m2 > 12:
    m2 = 1
    y2 = y2 + 1
m2_y2 = str(m2) + '_' + str(y2)

# Create your models here.

HOSTEL_CHOICES = (
        ('Barak', 'Barak'),
        ('Bramhaputra', 'Bramhaputra'),
        ('Dhansiri', 'Dhansiri'),
        ('Dibang', 'Dibang'),
        ('Dihing', 'Dihing'),
        ('Kameng', 'Kameng'),
        ('Kapili', 'Kapili'),
        ('Lohit', 'Lohit'),
        ('Manas', 'Manas'),
        ('Siang', 'Siang'),
        ('Subansiri', 'Subansiri'),
        ('Umiam', 'Umiam'),
    )
#Not final
FEEDBACK_CHOICES = (
    (1, ("Very Poor")),
    (2, ("Poor")),
    (3, ("Average")),
    (4, ("Neutral")),
    (5, ("Good")),
    (6, ("Very Good")),
)


class MessFeedback(models.Model):
    hostelName = models.CharField(max_length=255,choices = HOSTEL_CHOICES)
    username = models.CharField(max_length=255)
    cleanliness = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    qual_b = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    qual_l = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    qual_d = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    catering = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    filled = models.BooleanField(default=False)
    month = models.IntegerField(default=m1)
    year = models.IntegerField(default=y1)
    month_year = models.CharField(max_length=255,default=m1_y1)

    class Meta:
        verbose_name = "MessFeedback"
        verbose_name_plural = "MessFeedback"
        unique_together = ('username','month_year')
#add month, year (as pk along with username)
#add further comments field
    def __str__(self):
        return '%s_%s_%s_%s' % (self.id,self.hostelName, self.month, self.year)

#numbr of subscribptions
#hostel NAME
#hardcode formula
#month
#year
#username

class Preference(models.Model):
    hostelName = models.CharField(max_length=255,choices = HOSTEL_CHOICES)
    username = models.CharField(max_length=255,primary_key=True)
    month = models.IntegerField(default=m2)
    year = models.IntegerField(default=y2)
    month_year = models.CharField(max_length=255,default=m2_y2)
    h1 = models.CharField(max_length=255,choices = HOSTEL_CHOICES, blank=True)
    h2 = models.CharField(max_length=255,choices = HOSTEL_CHOICES, blank=True)
    h3 = models.CharField(max_length=255,choices = HOSTEL_CHOICES, blank=True)
    class Meta:
        verbose_name = "Preferences"
        verbose_name_plural = "Preferences"
        unique_together = ('username','month_year')

class Opi_calculated(models.Model):
    hostelName = models.CharField(max_length=255,choices = HOSTEL_CHOICES)
    opi_value = models.FloatField()
    numberOfSubscriptions = models.IntegerField() #actually no of feedback
    month = models.IntegerField(default=m1)
    year = models.IntegerField(default=y1)
    month_year = models.CharField(max_length=255,default=m1_y1)

    class Meta:
        verbose_name = "Opi_calculated"
        verbose_name_plural = "Opi_calculated"
        unique_together = ('hostelName','month_year')
    def __str__(self):
        return '%s_%s_%s' % (self.hostelName, self.month, self.year)


# createcachetable if db is renewed
