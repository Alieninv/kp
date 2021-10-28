from django.db import models
from django.contrib.auth.models import User
# Create your models here.
job_choice=[
    (1,'it'),
    (2,'nonit'),
    (3,'Pharma'),
    (4,'Bussiness'),
    (5,'selfemployee')
]
class Commoninfo(models.Model):
    name=models.CharField(max_length=30)
    phoneno=models.IntegerField(blank=True)
    state=models.CharField(max_length=20,blank=True)
    city=models.CharField(max_length=20,blank=True)
    address=models.CharField(max_length=50,blank=True)
    alternate_number=models.IntegerField(blank=True)
    class meta:
        abstract=True

class Hostell(Commoninfo):
    ownername=models.CharField(max_length=30,blank=True)
    wardenname=models.CharField(max_length=30,blank=True)
    phoneno = None
    alternate_number = None
    warden_phn=models.IntegerField(blank=True)
    warden_phn2=models.IntegerField(blank=True)
    owner_phno1=models.IntegerField(blank=True)
    owner_phno2=models.IntegerField(blank=True)
    startdate=models.DateField(blank=True)
    strength=models.IntegerField(blank=True)
    landmark=models.CharField(max_length=30,blank=True)
    def __str__(self):
        return 'hostel is ' + self.name


class Personn(Commoninfo):
    dateofjoin=models.DateField(blank=True)
    dateofbirth=models.DateField(blank=True)
    age=models.IntegerField(blank=True)
    heighest_qualification=models.CharField(max_length=20,blank=True)
    work=models.CharField(max_length=15,choices=job_choice,blank=True)
    company=models.CharField(max_length=50,blank=True)
    designation=models.CharField(max_length=30,blank=True)
    def __str__(self):
        return 'new person is '+self.name


class Student(models.Model):
   #user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
   #user=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True,limit_choices_to={'is_staff':True})
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    section=models.CharField(max_length=10)
    doj=models.DateField()







