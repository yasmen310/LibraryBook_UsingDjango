from django.shortcuts import render
from .models import Department
from .form import NewDepartment,NewBook
from django.shortcuts import redirect

# Create your views here.
def retriveData(request):
     x=Department.objects.all()
     return render(request,'Bookapp/retriveData.html',{'department':x})
def displayDepartment(request,dept_id):
    dept=Department.objects.get(pk=dept_id)
    return render(request,'Bookapp/department.html',{'Department':dept})

def newdepartment(request):
    form=NewDepartment(request.POST or None ,request.FILES or None)
    if form.is_valid():
       form.save()
       return redirect("all_department")
    return render(request,'Bookapp/newdepartment.html',{'form':form})

def newbook(request,dept_id):
     dept=Department.objects.get(pk=dept_id)
     form=NewBook(request.POST or None ,request.FILES or None)
     if form.is_valid():
         form=form.save(commit=False)
         form.dept=dept
         form.save()
         return redirect("department",dept_id=dept_id)
     return render(request,'Bookapp/newbook.html',{'Department':dept,'form':form})

from django.contrib.auth.forms import UserCreationForm
def signUp(request):
       form=UserCreationForm(request.POST or None ,request.FILES or None)
       if form.is_valid():
          form.save()
          return redirect("all_department")
       return render(request,'Bookapp/newuser.html',{'form':form})

from .form import MySignUpForm
from django.contrib.auth import login
def signcustomization(request):
       form=MySignUpForm(request.POST or None ,request.FILES or None)
       if form.is_valid():
          user=form.save()
          login(request,user)
          return redirect("all_department")
       return render(request,'Bookapp/newuser2.html',{'form':form})