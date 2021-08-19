from django.contrib import admin
from .models import Patient
from django.db import models
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','age')
    list_filter= ('test_date','age','treatment','patient_status')
