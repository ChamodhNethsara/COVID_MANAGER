from django.urls import path
from manager import views

app_name = 'manager'

urlpatterns= [
    path('',views.welcome,name='welcome'),
    path('all_patients/',views.all_patients,name='all_patients'),
    path('view_patient/<int:id>/',views.view_patient, name='view_patient'),
    path('delete_patient/<int:id>/', views.delete_patient,name='delete_patient'),
    path('add_patient_view/', views.add_patient_view,name='add_patient_view'),
    path('add_patient/', views.add_patient,name='add_patient'),




]
