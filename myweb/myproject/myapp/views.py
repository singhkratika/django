from django.shortcuts import render,redirect
from . models import Employee

# Create your views here.
def index(request):
    msg=''
    if request.method=="POST":
        empid=request.POST['empid']
        empname=request.POST['empname']
        department=request.POST['department']
        salary=request.POST['salary']
        emp=Employee(empid=empid,empname=empname,department=department,salary=salary)
        emp.save()
        msg='Registration is done.' 
    empinfo=Employee.objects.all()    
    return render(request,"index.html",{'msg':msg,'empinfo':empinfo})
def deleteemp(request,empid):
    emp=Employee.objects.get(empid=empid)
    emp.delete()
    return redirect('index')
def updateemp(request,empid):
    emp=Employee.objects.get(empid=empid)
    return render(request,"update.html",{'emp':emp})
def updatecode(request):
    empid=request.POST['empid']
    empname=request.POST['empname']
    department=request.POST['department']
    salary=request.POST['salary']
    Employee.objects.filter(empid=empid).update(empname=empname,department=department,salary=salary)
    return redirect('index')