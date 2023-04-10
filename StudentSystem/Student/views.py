"""
    This module defines views for a Student application. It includes functions for rendering 
    various pages of the application, such as the index, home, and about pages, as well as 
    functions for handling student-related actions like adding, updating, and 
    deleting student records. The module also imports the necessary forms and models
    from the student application.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SignupForm, StudentAddForm
from .models import Student, Domain


def index_view(request):
    """
    Function to render the index page of the application
    """
    domains = Domain.objects.all()
    return render(request, 'Student/index.html', {'domains': domains})


def student_home(request):
    """
    Function to render the home page of the application for students
    """
    domains = Domain.objects.all()
    return render(request, 'Student/home.html', {'domains': domains})


def student_show(request, pid):
    """
    Function to render the page for a specific domain
    """
    domains = get_object_or_404(Domain, pk=pid)
    return render(request, 'Student/show.html', {'domains': domains})


def student_privacy(request):
    """
    Function to render the privacy page of the application
    """
    return render(request, 'Student/privacy.html')


def student_about(request):
    """
    Function to render the about page of the application
    """
    return render(request, 'Student/about.html')


def student_contact(request):
    """
    Function to render the contact page of the application
    """
    return render(request, 'Student/contact.html')


def signupview(request):
    """
    Function to render the signup page of the application
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"You are successfully logged in as {username}!")
            return redirect('signin')
    elif request.method == "GET":
        form = SignupForm()
    return render(request, 'Student/signup.html', {'form': form})


def student_view(request):
    """
    Function to render the list of students in the application
    """
    student_list = Student.objects.all()
    return render(request, 'Student/viewStudent.html', {'student_list': student_list})


def student_add(request):
    """
    Function to add a new student to the application
    """
    if request.method == "POST":
        form = StudentAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            messages.success(request, f"Record is added for {first_name} {last_name}")
            return redirect('/list')
    elif request.method == "GET":
        form = StudentAddForm()
    return render(request, 'Student/addStudent.html', {'form': form})


def student_delete(request,id):
    """
    Function to delete a student from the application
    """
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('Student:list')
    return render(request, 'Student/deleteStudent.html', {'student': student})


def student_update(request, id):
    """
    Function to update a student's record in the application
    """
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = StudentAddForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            messages.success(request, f"Record is updated for {first_name} {last_name}")
            return redirect('Student:list')
        if not form.is_valid():
            print(form.errors)
    else:
        form = StudentAddForm(instance=student)
    return render(request, 'Student/updateStudent.html', {'form': form, 'student': student})
    