from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import Userf, Formuser, Nurse, HospitalForms, VaccinForms
from .models import verify, Vaccin, Hospital


def new_temp(request):
    return render(request, 'index.html')


# def new_user(request):
#     return render(request, 'User.html')
#
#
# def new_Nurse(request):
#     return render(request, 'Nurse.html')


def new_Admin(request):
    return render(request, 'admintemp/dashboard.html')


def customer_user(request):
    userform = Formuser()
    if request.method == 'POST':
        userform = Formuser(request.POST, request.FILES)
        if userform.is_valid():
            user = userform.save(commit=False)
            user.is_user = True
            user.save()
            return redirect('new_temp')
    return render(request, 'customer_reg.html', {'userform': userform})


def Nurse_form(request):
    physcicianform = Nurse()
    if request.method == 'POST':
        physcicianform = Nurse(request.POST, request.FILES)
        if physcicianform.is_valid():
            physcician = physcicianform.save(commit=False)
            physcician.is_Nurse = True
            physcician.save()
            return redirect('new_temp')
    return render(request, 'Nurse_reg.html', {'Note': physcicianform})


def All_form(request):
    allform = verify.objects.all()
    return render(request, 'allview.html', {'CustomForm': allform})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        print(username)
        password = request.POST.get('Password')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('new_Admin')
            elif user.is_user:
                return redirect('cust_log')
            elif user.is_Nurse:
                return redirect('nurse_log')
    return render(request, 'login.html')


#
# def vaccin_add(request):
#     form = VaccinForms()
#     if request.method == 'POST':
#         form= VaccinForms(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('vaccin_view')
#
#     return render(request, 'admintemp/vaccin_add.html', {'add': form})
# #
#
# def vaccin_view(request):
#     vaccin_details = Vaccin.objects.all()
#     return render(request, 'admintemp/vaccin_view.html', {'image':vaccin_details})
#
#
# def vaccin_update(request,id):
#     vaccinupdate = Vaccin.objects.get(id=id)
#     if request.method == 'POST':
#         updateForm = VaccinForms(request.POST, request.FILES, instance=vaccinupdate)
#         if updateForm.is_valid():
#             updateForm.save()
#             return redirect('vaccin_view')
#
#     else:
#         updateForm = VaccinForms(instance=vaccinupdate)
#         return render(request, 'admintemp/vaccin_update.html', {'updateform': updateForm})
#
#
# def vaccin_delete(request,dl):
#     vaccindelete=Vaccin.objects.get(id=dl)
#     vaccindelete.delete()
#     return redirect('vaccin_view')
#
def logout_view(request):
    logout(request)
    return redirect('new_temp')
