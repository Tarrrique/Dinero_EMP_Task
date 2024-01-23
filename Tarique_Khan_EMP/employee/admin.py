
from django.contrib import admin
from .models import Department, Employee, EmployeeSalary

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'reporting_manager', 'department')
    search_fields = ('name', 'email')
    list_filter = ('designation', 'department')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')
    search_fields = ('name',)
    list_filter = ('floor',)

class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'start_date', 'end_date')
    search_fields = ('employee__name',)
    list_filter = ('employee__department',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)
