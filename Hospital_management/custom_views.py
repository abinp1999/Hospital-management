from django.shortcuts import render, redirect
from .forms import Userf, Formuser, Nurse, HospitalForms, VaccinForms, ComplaintForms
from .models import verify, Vaccin, Hospital, complaints, Schedule_add, Appointment


def cust_log(request):
    return render(request, 'custom/dashboard.html')


def complaint_add(request):
    form = ComplaintForms()
    u = request.user
    print(u)
    if request.method == 'POST':
        form = ComplaintForms(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User = u
            obj.save()
            return redirect('complaint_view')
    return render(request, 'custom/complaint_add.html', {'form': form})


def complaint_view(request):
    complaint_details = complaints.objects.filter(User=request.user)
    return render(request, 'custom/complaint_view.html', {'image': complaint_details})


def complaint_update(request, id):
    complaintupdate = complaints.objects.get(id=id)
    if request.method == 'POST':
        updateForm = ComplaintForms(request.POST, request.FILES, instance=complaintupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('complaint_view')

    else:
        updateForm = ComplaintForms(instance=complaintupdate)
        return render(request, 'custom/complaint_update.html', {'updateForm': updateForm})


def complaint_delete(request, dl):
    complaintdelete = complaints.objects.get(id=dl)
    complaintdelete.delete()
    return redirect('complaint_view')


def custom_schedule_view(request):
    schedule_details = Schedule_add.objects.all()
    return render(request, 'custom/customer_schedule_view.html', {'schedule': schedule_details})


def book_add(request, id):
    schedule = Schedule_add.objects.get(id=id)
    u = request.user
    data = Appointment.objects.filter(user=u, schedule=schedule)
    if data.exists():
        print("booked")
    else:
        if request.method == 'POST':
            data = Appointment()
            data.schedule = schedule
            data.user = u
            data.save()
            return redirect('book_view')
    return render(request, 'custom/Booking.html', {'Book': schedule})


def book_view(request):
    view = Appointment.objects.filter(user=request.user)
    return render(request, 'custom/book_view.html', {'see': view})
