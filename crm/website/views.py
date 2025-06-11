from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from . forms import SignUpForm
from . models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
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
        return render(request,'website/home.html',{'records':records})




# logout ...
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out succesfully :)")
    return redirect('home')

# Register

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'You Have Logged in Successfully !!')
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'website/register.html',{'form':form})





