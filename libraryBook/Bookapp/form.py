from .models import Department,Book
from django import forms
class NewDepartment(forms.ModelForm):
      class Meta:
        model=Department
        fields='__all__'
class NewBook(forms.ModelForm):
      class Meta:
        model=Book
        exclude=['dept']

# custiomize usercreateform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MySignUpForm(UserCreationForm):
  first_name=forms.CharField(max_length=15)
  last_name=forms.CharField(max_length=15)
  email=forms.EmailField(max_length=15)
  class Meta:
    model=User
    fields=('first_name','last_name','email','username','password1','password2')