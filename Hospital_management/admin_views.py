from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import Userf, Formuser, Nurse, HospitalForms,VaccinForms,ComplaintForms
from .models import verify, Vaccin, Hospital,complaints,Appointment,Schedule_add


def admin_log(request):
    return render(request, 'admintemp/dashboard.html')


def hospital_add(request):
    form = HospitalForms()
    if request.method == 'POST':
        form = HospitalForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hospital_view')

    return render(request, 'admintemp/hospital_add.html', {'add': form})


def hospital_view(request):
    product_details = Hospital.objects.all()
    return render(request, 'admintemp/hospital_view.html', {'image': product_details})
#
def hospital_update(request, id):
    hospitalupdate = Hospital.objects.get(id=id)
    if request.method == 'POST':
        updateForm = HospitalForms(request.POST, request.FILES, instance=hospitalupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('hospital_view')

    else:
        updateForm = HospitalForms(instance=hospitalupdate)
        return render(request, 'admintemp/hospital_update.html', {'updateform': updateForm})


def hospital_delete(request,dl):
    ProdDelete=Hospital.objects.get(id=dl)
    ProdDelete.delete()
    return redirect('hospital_view')


def vaccin_add(request):
    form = VaccinForms()
    if request.method == 'POST':
        form= VaccinForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vaccin_view')

    return render(request, 'admintemp/vaccin_add.html', {'form': form})


def vaccin_view(request):
    vaccin_details = Vaccin.objects.all()
    return render(request, 'admintemp/vaccin_view.html', {'image':vaccin_details})


def vaccin_update(request,id):
    vaccinupdate = Vaccin.objects.get(id=id)
    if request.method == 'POST':
        updateForm = VaccinForms(request.POST, request.FILES, instance=vaccinupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('vaccin_view')

    else:
        updateForm = VaccinForms(instance=vaccinupdate)
        return render(request, 'admintemp/vaccin_update.html', {'update': updateForm})


def vaccin_delete(request,dl):
    vaccindelete=Vaccin.objects.get(id=dl)
    vaccindelete.delete()
    return redirect('vaccin_view')

def admin_reply(request):
    complaint_details = complaints.objects.all()
    return render(request, 'admintemp/complaint_view.html', {'complaint':complaint_details})

def reply_now(request,id):
    complaint = complaints.objects.get(id=id)
    if request.method == 'POST':
        r =request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        return redirect('admin_reply')
    return render(request, 'admintemp/Reply_now.html',{'complaint':complaint})

def reply_edit(request,id):
    compedit = complaints.objects.get(id=id)
    if request.method == 'POST':
        edit = ComplaintForms(request.POST, instance=compedit)
        if edit.is_valid():
            edit.save()
            return redirect('reply_edit')

    else:
        edit = ComplaintForms(instance=compedit)
        return render(request, 'admintemp/complaint_view.html', {'edit': edit})

def appoinment_view(request):
    see = Appointment.objects.all()
    return render (request,'admintemp/Appoinment.html',{'after':see})



def accept_appointment(request,id):
    appointments = Appointment.objects.get(id=id)

    obj = appointments
    obj.status = 1
    print(obj.status)
    obj.save()
    return redirect('appoinment_view')

def reject_appointment(request,id):
    appointments = Appointment.objects.get(id=id)
    obj = appointments
    obj.status = 2
    obj.save()

    return redirect('appoinment_view')






