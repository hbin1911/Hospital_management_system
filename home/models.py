from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    date=models.DateField(auto_now_add=True,blank=True)

    def __str__ (self):
        return "Message from " + self.name #+ ' - ' + self.email


class Patient(models.Model):
    patient_Name = models.CharField(max_length=100)
    # date_of_birth = models.DateField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.TextField()
    gender = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.patient_Name

class Book(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    number = models.IntegerField()
    desc = models.TextField()
    date = models.DateField(auto_now_add=True,blank=True)

    def __str__ (self):
        return "Appointment from " + self.name #+ ' - ' + self.email

class Doctor(models.Model):
    doctor_Name = models.CharField(max_length=100)
    agee = models.IntegerField()
    phonee = models.IntegerField()
    emaill = models.EmailField(max_length=100)
    genderr = models.CharField(max_length=50)
    addresss = models.TextField()
    roless = models.TextField()
    
    def __str__(self):
        return self.doctor_Name


class Room(models.Model):
    roomnumber = models.IntegerField()
    roomtype = models.CharField(max_length=50)
    patientname = models.CharField(max_length=100)
    allotmentdte = models.CharField(max_length=50)
    dischargedte =models.CharField(max_length=50)
    docname = models.CharField(max_length=100)

    def __str__ (self):
        return "Room Alloted - " + self.roomtype + " " + "For " + self.patientname #+ ' - ' + self.email