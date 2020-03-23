from django.shortcuts import render,redirect
from .forms import InsertEmployeeData,UpdateEmployeeData,DeleteEmployeeData
from .models import EmpployeeData
from django.http.response import HttpResponse
from django.contrib import messages

def home_page(request):
    return render(request, 'curd/home_page.html')


def create_view(request):
    iform = InsertEmployeeData()
    context = {'iform':iform}

    if request.method =="POST":
        iform = InsertEmployeeData(request.POST)
        if iform.is_valid():
            empid = request.POST.get('emp_id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            salary = request.POST.get('salary')
            location = request.POST.get('location')
            company = request.POST.get('company')

            data = EmpployeeData(
            first_name=first_name,
            emp_id=empid,
            last_name=last_name,
            email=email,
            mobile=mobile,
            salary=salary,
            location=location,
            company=company
            )
            data.save()
            return render(request,'curd/create_page.html',context)
    return render(request,'curd/create_page.html',context)

# Create your views here.
def update_view(request):
    if request.method == "POST":
        uform = UpdateEmployeeData(request.POST)
        if uform.is_valid():
            empid = request.POST.get('emp_id')
            salary = request.POST.get('salary')
            eid = EmpployeeData.objects.filter(emp_id=empid)
            if not eid :
                return redirect('no-data')
            else:
                eid.update(salary=salary)
                uform = UpdateEmployeeData()
                context = {'uform': uform}
                return render(request, 'curd/update_page.html', context)
    else:
                uform = UpdateEmployeeData()
                context = {'uform':uform}
                return render(request,'curd/update_page.html',context)


def retrieve_view(request):
    data = EmpployeeData.objects.all()
    context = {'data':data}
    return render(request,'curd/retrieve_page.html',context)

def delete_view(request):
    if request.method == "POST":
        dform = DeleteEmployeeData(request.POST)
        if dform.is_valid():
            empid = request.POST.get('emp_id')
            eid = EmpployeeData.objects.filter(emp_id=empid)
            if eid:
                eid.delete()
                dform = DeleteEmployeeData()
                context = {"dform": dform}
                return render(request, 'curd/delete_page.html', context)
        else:
                messages.warning(request, 'Incorrect Employee ID')
                return redirect('delete')
    else:
                dform = DeleteEmployeeData()
                context = {"dform":dform}
                return render(request,'curd/delete_page.html',context)

