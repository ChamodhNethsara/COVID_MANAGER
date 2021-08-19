from django.core import paginator
from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages 
from .forms import Add_Patient_form
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def welcome(request):
    form = Add_Patient_form
    return render(request,'manager/index.html',{'form': form})

@login_required
def all_patients(request):
    if request.GET.get('search'):
        query = request.GET.get('search')
        patients = Patient.objects.filter(name__contains=query)
        paginator = Paginator(patients,25)
    else:

        patients = Patient.objects.all()
        paginator = Paginator(patients,25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'manager/all_patients.html',{'patients': page_obj})

@login_required
def add_patient_view(request):
    return render(request,'manager/add_patient.html',{'form':Add_Patient_form})





@login_required
def add_patient(request):
    patient = Add_Patient_form(request.POST)
    if patient.is_valid():
        patient.save()
    
        
        return HttpResponseRedirect(reverse('manager:all_patients'))
    
    


@login_required
def view_patient(request,id):
    patient = Patient.objects.get(id=id)

    return render(request,'manager/view_patient.html',{'patient':patient})

@login_required
def delete_patient(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    all_patients(request)



