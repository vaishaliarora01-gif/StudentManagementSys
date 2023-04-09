from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Student.models import Student


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        
class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stu_num', 'first_name', 'last_name', 'email', 'image', 'gpa', 'domain']
        widgets = {
            'stu_num': forms.TextInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'first_name': forms.TextInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'last_name': forms.TextInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'email': forms.EmailInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'image': forms.ClearableFileInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'gpa': forms.NumberInput(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
            'domain': forms.Select(attrs={'style': 'border: 2px solid teal; width: 100%;'}),
        }

        
       