"""
This module contains forms used in the Student app.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Student.models import Student


class SignupForm(UserCreationForm):
    """
    A form that inherits from UserCreationForm to add additional fields for sign up.

    Attributes:
    -----------
    email : forms.EmailField
        Email field for the user's email address.
    first_name : forms.CharField
        Char field for the user's first name.
    last_name : forms.CharField
        Char field for the user's last name.
    
    Methods:
    --------
    Meta:
        Meta class to specify the model and fields for the form.
    """

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        """
        Meta class to specify the model and fields for the SignupForm.

        Attributes:
        -----------
        model : django.contrib.auth.models.User
            User model for the form.
        fields : list
            List of fields to include in the form.
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        
class StudentAddForm(forms.ModelForm):
    """
    A form to add a new student.

    Attributes:
    -----------
    Meta:
        Meta class to specify the model and fields for the form.
    """

    class Meta:
        """
        Meta class to specify the model and fields for the StudentAddForm.

        Attributes:
        -----------
        model : Student.models.Student
            Student model for the form.
        fields : list
            List of fields to include in the form.
        widgets : dict
            A dictionary of widgets to customize the form's HTML.
        """
        model = Student
        fields = ['stu_num', 'first_name', 'last_name', 'email', 'image', 'gpa', 'domain']
        widgets = {
            'stu_num': forms.TextInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'first_name': forms.TextInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'last_name': forms.TextInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'email': forms.EmailInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'image': forms.ClearableFileInput(attrs=
                          {'style': 'border: 2px solid teal;width: 100%;'}),
            'gpa': forms.NumberInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'domain': forms.Select(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
        }
