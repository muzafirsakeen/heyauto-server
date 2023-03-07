from django import forms 
from .models import  driver_detail

class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = driver_detail 
        fields = ['d_name', 'd_photo','d_email','d_phone','d_password','d_age','d_gender'] 



       