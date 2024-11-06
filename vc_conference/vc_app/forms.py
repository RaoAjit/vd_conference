from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class register(UserCreationForm):
    name=forms.CharField(required=True,max_length=100)
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=('name','email','password1','password2')

    def save(self, commit=True):
        user=super(register,self).save(commit=False)
        user.name=self.cleaned_data['name']
        user.email=self.cleaned_data['email']
        user.username=self.cleaned_data['name']
      

        if commit:
            user.save()
        return user
        
