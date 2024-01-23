from django.shortcuts import render, HttpResponseRedirect

from .models import *


def base(req):
    data = Department.objects.all()
    print(data[0].id)
    print(data)
    return render(req, 'employee/base.html', {

        'data': data})


def add_emp(request, department_id):

    dep = Department.objects.get(pk=department_id)

    data = Employee.objects.filter(department=dep)
    return render(request, 'employee/emp.html', {

        'data': data,
        'dep': dep})


def add_department(request):

    data = Department.objects.all()
    return render(request, 'employee/department.html', {

        'data': data})


def add_salary(request, department_id):

    department = Department.objects.get(pk=department_id)
    employees = department.employee_set.all()

    salary_data = EmployeeSalary.objects.filter(employee__in=employees)

    return render(request, 'employee/salary.html', {
        'department': department,
        'employees': employees,
        'salary_data': salary_data,
    })


def salary_report(request):
    form = SalaryReportForm(request.GET or None)
    salary_data = []

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        salary_data = get_salary_data(start_date, end_date)

    return render(request, 'employee/salary_report.html', {'form': form, 'salary_data': salary_data})


def get_salary_data(start_date, end_date):

    data = EmployeeSalary.objects.filter(
        start_date__range=[start_date, end_date]
    ).values('employee__department__name').annotate(total_cost=models.Sum('salary'))

    salary_data = [(entry['employee__department__name'],
                    entry['total_cost']) for entry in data]
    return salary_data


def department_reporting(request, department_id):
    department = Department.objects.get(pk=department_id)
    manager = Employee.objects.get(
        department=department, designation='Manager')

    hierarchy = get_hierarchy(manager)
    print(department)
    print(hierarchy['manager'].name)

    return render(request, 'employee/department_reporting.html', {'department': department, 'hierarchy': hierarchy})


def get_hierarchy(manager):
    hierarchy = {'manager': manager, 'tl_list': []}

    tl_list = Employee.objects.filter(
        reporting_manager=manager, designation='TL')

    for tl in tl_list:
        associates = get_hierarchy_for_tl(tl)
        hierarchy['tl_list'].append({'tl': tl, 'associates': associates})

    return hierarchy


def get_hierarchy_for_tl(tl):
    associates = Employee.objects.filter(
        reporting_manager=tl, designation='Associate')
    hierarchy = []

    for associate in associates:
        associate_hierarchy = get_hierarchy_for_tl(associate)
        hierarchy.append(
            {'associate': associate, 'subordinates': associate_hierarchy})

    return hierarchy

