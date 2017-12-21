from django.db import models

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
    class Meta:
        verbose_name = "MessFeedback"
        verbose_name_plural = "MessFeedback"
    hostelName = models.CharField(max_length=255,choices = HOSTEL_CHOICES)
    username = models.CharField(max_length=255,primary_key=True)
    cleanliness = models.CharField(max_length=255,choices = FEEDBACK_CHOICES,null=True)
    qual_b = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    qual_l = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    qual_d = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    catering = models.IntegerField(choices = FEEDBACK_CHOICES,null=True)
    filled = models.BooleanField(default=False)
    month = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
#add month, year (as pk along with username)
    def __str__(self):
        return '%s_%s_%s' % (self.hostelName, self.month, self.year)

#numbr of subscribptions
#hostel NAME
#hardcode formula
#month
#year
#username

class Opi_calculated(models.Model):
    class Meta:
        verbose_name = "Opi_calculated"
        verbose_name_plural = "Opi_calculated"
    hostelName = models.CharField(max_length=255,choices = HOSTEL_CHOICES)
    month = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    opi_value = models.IntegerField()
    numberOfSubscriptions = models.IntegerField()
        def __str__(self):
            return '%s_%s_%s' % (self.hostelName, self.month, self.year)
