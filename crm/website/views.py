from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check if user is loging...
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Loged in successfully !!")
            return redirect('home')
        else:
            messages.error(request,"Username or password may be incorrect...Try Again")
            return redirect('home')

    

    else:
        return render(request,'website/home.html',{})




# logout ...
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out succesfully :)")
    return redirect('home')

  
