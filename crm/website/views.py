from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from . forms import SignUpForm , AddRecordForm
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


def record_user(request, pk):
    if request.user.is_authenticated:
        try:
            record = Record.objects.get(id=pk)
            return render(request, 'website/record.html', {'record': record})
        except Record.DoesNotExist:
            messages.error(request, 'Record not found.')
            return redirect('home')
    else:
        messages.warning(request, 'You must be logged in to view this page!')
        return redirect('home')


def delete_record_user(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record deleted Sucessesfully !!")
        return redirect('home')
    else:
        messages.error(request,"You msut be logged in to delete the record")
        return redirect('home')

def add_record_user(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Added sucessfully")
                return redirect('home')
        return render(request,'website/add_record.html',{'form':form})
    else:
        messages.error(request,"Must login to add record")
        return redirect('home')
    
def update_record_user(request,pk):
    if request.user.is_authenticated:
        cur_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None , instance=cur_record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Record Updated Sucessfully :)")
                return redirect('home')
        return render(request,'website/update_record.html',{'form':form})
    else:
        messages.error(request,"Must login to Update")
        return redirect('home')



