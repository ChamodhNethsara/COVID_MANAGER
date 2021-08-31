from django import forms
from django.forms import ModelForm, widgets
from .models import Patient

class Add_Patient_form(ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name',
            'age',
            'address',
            'family_info',
            'test_date',
            'treatment',
            'treatment_place',
            'telephone',
            'patient_status'
        ]
    def __init__(self, *args, **kwargs):
        super(Add_Patient_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            




        
        

    
