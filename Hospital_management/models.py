from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=250)
    email_id = models.CharField(max_length=250)
    phone_no = models.IntegerField()
    image = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name


class verify(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_Nurse = models.BooleanField(default=False)
    gender = models.CharField(max_length=50, null=True)
    phone_no = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True)
    image = models.FileField(upload_to='upon/')
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING, blank=True, null=True)


class Vaccin(models.Model):
    name = models.CharField(max_length=250)
    ex_date = models.DateField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class complaints(models.Model):
    User = models.ForeignKey(verify, on_delete=models.DO_NOTHING, blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    reply = models.CharField(max_length=300, blank=True, null=True)
    complaint = models.CharField(max_length=300, blank=True, null=True)


class Schedule_add(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING, blank=True, null=True)
    vaccine = models.ForeignKey(Vaccin, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    schedule = models.ForeignKey(Schedule_add, on_delete=models.CASCADE)
    user = models.ForeignKey(verify, on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0)
