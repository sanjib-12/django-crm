from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


# Create your views here.
def home(request):
   records = Record.objects.all()
   
   # check to see if logging in 
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      # Authenticate
      user = authenticate(request, username=username, password=password)
      if(user is not None):
         login(request, user)
         messages.success(request, "You Have Been Logged In!")
         return redirect('home')
      else:
         messages.success(request, "There was an Error Logging In, Please try Again")
         return redirect('home')
   
   else:
      return render(request, 'home.html', {'records':records})


def logout_user(request):
   logout(request)
   messages.success(request, "you Have Been Logged Out ... ")
   return redirect('home')

def register_user(request):
   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         #Authenticate and login
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         
         user  = authenticate(username=username, password=password)
         login(request, user)
         messages.success(request, "you Have Successfully Registered")
         return redirect('home')
   else:
      form = SignUpForm()
      return render(request, 'register.html', {'form': form})
   return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
   if request.user.is_authenticated:
      customer_record = Record.objects.get(id=pk)
      return render(request, 'record.html', {'customer_record': customer_record})
   else:
      messages.success(request, "you must be logged in to view that page... ")
      return redirect('home')
   

def delete_record(request, pk):
   if request.user.is_authenticated:
      delete_it = Record.objects.get(id=pk)
      delete_it.delete()
      messages.success(request, "Records Deleted Successfully")
      return redirect('home')
   else:
      messages.success(request, "You must be logged in to do that...")
      return redirect('home')
   
def add_record(request):
   return render(request, 'add_record.html', {})