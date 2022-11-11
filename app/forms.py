from django import forms
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
    

class BlogInfoForm(forms.ModelForm):
    class Meta:
        model=BlogInfo
        fields=['data','blogs']
        






























        