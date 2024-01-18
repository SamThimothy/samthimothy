from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentsForm,SignUpForm
from .models import StudentsModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count

# Create your views here.
def home_view(request):
    return render(request,'testapp1/home.html')

def python_view(request):
    return render(request,'testapp1/python.html')

def java_view(request):
    return render(request,'testapp1/java.html')

def students_form_view(request):
    form=StudentsModel.objects.all()
    if request.method=="POST":
        data=StudentsForm(request.POST)
        if data.is_valid():
            data.save(commit=True)
            print('Students')
            print('Information')
            print('Saved!!!!')
            return redirect('/app1/sdata')
    return render(request,'testapp1/studentsform.html',{'form':form})

@login_required
def students_display_view(request):
    data=StudentsModel.objects.all()
    return render(request,'testapp1/studentsdisplay.html',{'data':data})

def students_delete_view(request,no):
    data=StudentsModel.objects.get(id=no)
    data.delete()
    return redirect('/app1/sdata')

def students_update_view(request,no):
    data=StudentsModel.objects.get(id=no)
    if request.method=='POST':
        ndata=StudentsForm(request.POST,instance=data)
        if ndata.is_valid():
            ndata.save(commit=True)
            print('Students')
            print('Information')
            print('Updated!!!!')
            return redirect('/app1/sdata')
    return render(request,'testapp1/studentsupdate.html',{'data':data})

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')
    return render(request,'testapp1/signup.html',{'form':form})

def login_view(request):
    return render(request,'testapp1/logout.html')

#dummy for testing

def demo_view(request):
    data1=StudentsModel.objects.filter(sname__contains='s').aggregate(Avg('smark'))
    return render(request,'testapp1/demo.html',{'data1':data1})
