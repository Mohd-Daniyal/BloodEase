from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User

def donor_signup_view(request):
    userForm=forms.DonorUserForm()
    donorForm=forms.DonorForm()
    mydict={'userForm':userForm,'donorForm':donorForm}
    if request.method=='POST':
        userForm=forms.DonorUserForm(request.POST)
        donorForm=forms.DonorForm(request.POST,request.FILES)
        if userForm.is_valid() and donorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            donor=donorForm.save(commit=False)
            donor.user=user
            donor.bloodgroup=donorForm.cleaned_data['bloodgroup']
            donor.save()
            my_donor_group = Group.objects.get_or_create(name='DONOR')
            my_donor_group[0].user_set.add(user)
            return HttpResponseRedirect('donorlogin')
        else:
            for field, errors in userForm.errors.items():
                for error in errors:
                    messages.error(request, f"*{field} {error}")
            
            for field, errors in donorForm.errors.items():
                for error in errors:
                    messages.error(request, f"*{field}: {error}")

    return render(request,'donor/donorsignup.html',context=mydict)

def donor_dashboard_view(request):
    donor= models.Donor.objects.get(user_id=request.user.id)
    dict={
        'requestpending': models.BloodDonate.objects.all().filter(donor=donor).filter(status='Pending').count(),
        'requestapproved': models.BloodDonate.objects.all().filter(donor=donor).filter(status='Approved').count(),
        'requestmade': models.BloodDonate.objects.all().filter(donor=donor).count(),
        'requestrejected': models.BloodDonate.objects.all().filter(donor=donor).filter(status='Rejected').count(),
        'username': models.Donor.objects.get(user_id=request.user.id).get_name
    }
    return render(request,'donor/donor_dashboard.html',context=dict)

def donate_blood_view(request):
    donation_form=forms.DonationForm()
    if request.method=='POST':
        donation_form=forms.DonationForm(request.POST)
        if donation_form.is_valid():
            blood_donate=donation_form.save(commit=False)
            donor=models.Donor.objects.get(user_id=request.user.id)
            blood_donate.donor=donor
            blood_donate.bloodgroup=donor.bloodgroup
            blood_donate.save()
            return HttpResponseRedirect('donation-history')  
    return render(request,'donor/donate_blood.html',{'donation_form':donation_form})

def donation_history_view(request):
    donor= models.Donor.objects.get(user_id=request.user.id)
    donations=models.BloodDonate.objects.all().filter(donor=donor)
    return render(request,'donor/donation_history.html',{'donations':donations})