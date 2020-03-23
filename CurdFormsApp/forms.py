from django import forms

class InsertEmployeeData(forms.Form):
    emp_id = forms.IntegerField (
        label="Enter Employee Number",
        widget=forms.NumberInput (
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Number'
            }
        )
    )


    first_name = forms.CharField(
        label="Enter Employee First Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee First Name'
            }
        )
    )

    last_name = forms.CharField(
        label="Enter Employee Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Last Name'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Employee Email ID",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Email ID'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter Employee Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Mobile Number'
            }
        )
    )

    salary = forms.IntegerField(
        label="Enter Employee Salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Salary'
            }
        )
    )

    location = forms.CharField(
        label="Enter Employee Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Location'
            }
        )
    )

    company = forms.CharField(
        label="Enter Employee Company Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Company Name'
            }
        )
    )
class UpdateEmployeeData(forms.Form):
    emp_id = forms.IntegerField(
        label="Enter Employee Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Number'
            }
        )
    )

    salary = forms.IntegerField(
        label="Enter Employee Salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Salary'
            }
        )
    )

class DeleteEmployeeData(forms.Form):
    emp_id = forms.IntegerField(
        label="Enter Employee Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Number'
            }
        )
    )


