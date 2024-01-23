# employee/models.py
from django.db import models
from django import forms

class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('Associate', 'Associate'),
        ('TL', 'TL'),
        ('Manager', 'Manager'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}-{self.name} in {self.department.name}"

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.salary} ({self.start_date} to {self.end_date})"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'



class SalaryReportForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))

