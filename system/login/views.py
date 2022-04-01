from django.contrib import messages
from multiprocessing import context
from .models import  Contact
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from login.forms import ContactForm, EmployeeRegistation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

def login_page(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')

        user =authenticate(request,username=username,password=password) 

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Username OR Password does not exits')


    context={}
    return  render(request, 'login_page.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def signup(request):
    # form.py use for to get some selected field for signup 
    #is_valid & cleaned_data method use for store clean and valid data in database.
    #make_password method use to store an  password in hash form.
    form = EmployeeRegistation()

    if request.method =='POST':
        form=EmployeeRegistation(request.POST)
        #is_valid & cleaned_data method use for store clean and valid data in database.
        #make_password method use to store an  password in hash form.
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=make_password(form.cleaned_data['password'])

            reg =User(first_name=first_name,last_name=last_name,
            username=username,
            email=email,
            password=password
            
            
            )
            reg.save()
            #login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registation please Try Again')

    return render(request, 'signup_page.html', {'form':form})

def contact(request):
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']

            con = Contact(name=name,email=email,message=message)
            con.save()
            return redirect('home')
        else:
            messages.error(request, 'Enter Vaild Details')
   
    return render(request, 'contact.html',{'form':form})

def about(request):
    return render(request, 'about.html')