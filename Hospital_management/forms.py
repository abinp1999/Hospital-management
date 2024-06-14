from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
import datetime

from .models import verify, Vaccin, Hospital, complaints, Schedule_add ,Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class Userf(forms.ModelForm):
    class Meta:
        model = verify
        fields = '__all__'


class Formuser(UserCreationForm):
    class Meta:
        model = verify
        fields = (
            'first_name', 'gender', 'phone_no', 'occupation', 'image', 'username', 'password1', 'password2', 'hospital')


class Nurse(UserCreationForm):
    class Meta:
        model = verify
        fields = ('first_name', 'gender', 'phone_no', 'occupation', 'username', 'password1', 'password2', 'hospital')


class HospitalForms(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'


class VaccinForms(forms.ModelForm):
    class Meta:
        model = Vaccin
        fields = '__all__'


class ComplaintForms(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = complaints
        fields = ('subject', 'date', 'complaint')


class ScheduleForms(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Schedule_add
        fields = ('hospital','vaccine', 'date', 'start_time', 'end_time',)


class BookForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Schedule_add
        fields = ('hospital','vaccine', 'date', 'start_time', 'end_time')

