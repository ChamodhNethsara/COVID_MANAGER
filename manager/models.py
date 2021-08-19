from django.db import models
from django.utils import timezone
#from .views import view_patient
from django.urls import reverse
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    family_info = models.TextField(blank=True)
    test_choices = [
        ('PCR','PCR'),
        ('Antigen','Antigen'),
    ]
    tests = models.CharField(choices=test_choices,max_length=50)
    test_date = models.DateField(verbose_name='Tested Date',
                                            default=timezone.now)
    treatments =[
        ('Home','Home'),
        ('Workplace','Workplace'),
        ('Hospital','Hospital')
    ]
    treatment = models.CharField(max_length=20,choices=treatments)
    treatment_place = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=10)

    status = [
        ('Tested Positive', 'Positive'),
        ('Quarntined','Qurantined'),
        ('Dead','Dead')
    ]

    patient_status = models.CharField(max_length=25, choices=status)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager:view_patient',args=[self.id])
        

    

    
    
    