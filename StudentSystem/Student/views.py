from django.shortcuts import render,redirect,get_object_or_404
from Student.forms import SignupForm,StudentAddForm
from django.contrib import messages
from Student.models import Student,Domain


# Create your views here.

def index_view(request):
    domains=Domain.objects.all()
    return render(request,'Student/index.html',{'domains':domains})

def student_home(request):
    domains=Domain.objects.all()
    return render(request,'Student/home.html',{'domains':domains})
    
def student_show(request,pid):
    domains=Domain.objects.get(pk=pid)
    print(domains)
    return render(request,'Student/show.html',{'domains':domains})
    
def student_privacy(request):
    return render(request,'Student/privacy.html')


def student_about(request):
    return render(request,'Student/about.html')
def student_contact(request):
    return render(request,'Student/contact.html')

def signupview(request):
        if request.method=="POST":
           form=SignupForm(request.POST)
           if form.is_valid():
               form.save()
               un=form.cleaned_data['username']
               messages.success(request,"You are successfully logged in as {}!!!!".format(un))
               return redirect('signin')
        elif request.method=="GET":
           form=SignupForm()
        return render(request,'Student/signup.html',{'form':form})
        
        
def student_view(request):
         student_list=Student.objects.all()
         return render(request,'Student/viewStudent.html',{'student_list':student_list})
       
 
       
def student_add(request):
        if request.method== "POST":
           form =StudentAddForm(request.POST,request.FILES)
           if form.is_valid():
               form.save()
               fn=form.cleaned_data['first_name']
               ln=form.cleaned_data['last_name']
               messages.success(request,"Record is added for {} {}".format(fn,ln))
               return redirect('/list')
        elif request.method=="GET":
                form=StudentAddForm()
        return render(request,'Student/addStudent.html',{'form':form})
        
        
def student_delete(request,id):
    student=Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('Student:list')
    return render(request,'Student/deleteStudent.html',{'student':student})
    


def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentAddForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            print("HI")    
            form.save()
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            messages.success(request, "Record is updated for {} {}".format(fn, ln))
            return redirect('Student:list')
        if not form.is_valid():
             print(form.errors)
    else:
        form = StudentAddForm(instance=student)
    return render(request, 'Student/updateStudent.html', {'form': form, 'student': student})

    
    
