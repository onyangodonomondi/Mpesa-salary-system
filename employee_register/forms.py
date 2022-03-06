from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','Mpesa_No','emp_code','position', 'Email', 'Salary')
        labels = {
            'fullname':'Full Name',
            'Mpesa_No' : "Mpesa_No",
            'emp_code':'EMP. Code',
            'Email': "Email",
            
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['Salary'].empty_label = "Select"
        self.fields['emp_code'].required = False
