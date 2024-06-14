from django.shortcuts import render, redirect
from .forms import Userf, Formuser, Nurse, HospitalForms, VaccinForms, ComplaintForms, ScheduleForms
from .models import verify, Vaccin, Hospital, complaints, Schedule_add
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def nurse_log(request):
    return render(request, 'nurse/dashboard.html')


def nurse_complaint_add(request):
    form = ComplaintForms()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForms(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User = u
            obj.save()
            return redirect('nurse_complaint_view')
    print(form)
    return render(request, 'nurse/nurse_complaint_add.html', {'form': form})


def nurse_complaint_view(request):
    complaint_details = complaints.objects.filter(User=request.user)
    return render(request, 'nurse/nurse_complaint_view.html', {'image': complaint_details})


def nurse_complaint_update(request, id):
    complaintupdate = complaints.objects.get(id=id)
    if request.method == 'POST':
        update = ComplaintForms(request.POST, request.FILES, instance=complaintupdate)
        if update.is_valid():
            update.save()
            return redirect('nurse_complaint_view')

    else:
        updateForm = ComplaintForms(instance=complaintupdate)
        return render(request, 'nurse/nurse_complaint_update.html', {'updateform': updateForm})


def nurse_complaint_delete(request, dl):
    complaintdelete = complaints.objects.get(id=dl)
    complaintdelete.delete()
    return redirect('nurse_complaint_view')


def schedule_add(request):
    alt = ScheduleForms()
    n = request.user
    d = verify.objects.get(username = n)
    print(d)
    u = d.hospital
    print(u)
    if request.method == 'POST':
        alt = ScheduleForms(request.POST)
        print(alt)
        if alt.is_valid():
            obj = alt.save(commit=False)
            obj.hospital = u
            obj.save()
            return redirect('schedule_view')
    return render(request, 'nurse/schedule_add.html', {'schedule': alt})


def schedule_view(request):
    schedule_details = Schedule_add.objects.all()
    return render(request, 'nurse/schedule_view.html', {'schedule': schedule_details})


def schedule_update(request,id):
    scheduleupdate = Schedule_add.objects.get(id=id)
    if request.method == 'POST':
        updateForm = ScheduleForms(request.POST, request.FILES, instance= scheduleupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('schedule_view')

    else:
        updateForm = ScheduleForms(instance= scheduleupdate)
        return render(request, 'nurse/schedule_update.html', {'updateform': updateForm})


def schedule_delete(request,dl):
    scheduletdelete=Schedule_add.objects.get(id=dl)
    scheduletdelete.delete()
    return redirect('schedule_view')