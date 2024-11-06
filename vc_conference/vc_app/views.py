from django.shortcuts import render,HttpResponse,redirect
from vc_app.forms import register
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def myregister(request):  
     if request.method == 'POST': 
          password1=request.POST.get('password1')
          password2=request.POST.get('password2')
          if password1 == password2:
                 form=register(request.POST) 
                 if form.is_valid():
                        form.save()
                        messages.success(request,'You have successfully Registerd')
                        return render(request,'login.html')
                 else:
                        messages.error(request, 'There was an error with your submission.')
                        return redirect('myregister')
                 
          else:
                    messages.error(request, 'Your both password are not matching.')
                    return render(request,'register.html')
               
                
     else:
            return render(request,'register.html')
               
        
         




def mylogin(request):
           if request.method =='POST':
                 username=request.POST.get('name')
                 password=request.POST.get('password')
                 user=authenticate(request,username=username,password=password)
                 if user is not None:
                       login(request,user)
                       return redirect('dashboard')  # Adjust to your success URL
                 else:
                        return render(request,'login.html')
                  
           else:
                  return render(request,'login.html')
                 
@login_required         
def dashboard(request):
      
      return render(request,'home.html')

@login_required   
def runvc(request):
      return render(request,'vc.html',{'name':request.user})

@login_required   
def mylogout(request):
      logout(request)
      return redirect('mylogin')

@login_required   
def joinroom(request):
      if request.method == 'POST':
            roomid=request.POST.get('roomid')
            return redirect('/meeting?roomID='+roomid)

      return render(request,'joinroom.html')
    
