import django
from django.contrib.auth.forms import UserCreationForm
from django.forms.forms import Form
from django.http.response import HttpResponse 
from django.shortcuts import render
from django.http import HttpResponse 
from .models import * 
from django.shortcuts import redirect, render
from .forms import *
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





from django.views import View
# Create your views here.


def home(request): 
    data= indeximg.objects.all()
    return render(request, 'main/index1.html', {'data':data})

def about(request):
    return render(request, 'main/about1.html')

def services(request):
    return render(request, 'main/typography.html')

def portfolio(request):
        return render(request, 'main/portfolio.html')

def single(request):
        return render(request, 'main/single.html')

def registerPage(request):
        if request.user.is_authenticated:
                return redirect('index1')
        else:
                form = UserCreationForm()

                if request.method == 'POST':
                        form = UserCreationForm(request.POST)
                        if form.is_valid():
                                form.save()
                                user = form.cleaned_data.get('username')
                                messages.success(request , 'Account was created for ' + user)
                                return redirect('login')

                context = {'form': form}
                return render(request, 'main/reg_form.html', context)


def loginPage(request):
        if request.user.is_authenticated:
                return redirect('index1')
        else:
                if request.method == 'POST':
                        username = request.POST.get('username')
                        password = request.POST.get('password')

                        user = authenticate(request, username=username, password=password)

                        if user is not None:
                                login(request, user)
                                return redirect('index1')
                        else:
                                messages.info(request, 'Username OR Password is incorrect')
                        

        context = {}
        return render(request, 'main/login.html', context)
 
def logoutUser(request):
        logout(request)
        return redirect('login') 

@login_required(login_url='login')      
def contact(request):

        if request.method== "POST":
               name=request.POST.get('name')
               email=request.POST.get('email')
               subject=request.POST.get('subject')
               message=request.POST.get('message')
               print(name,email,subject,message)
               ins= Contact(name=name ,email=email, subject=subject, message=message)
               ins.save()
               
        return render(request, 'main/contact.html')
@login_required(login_url='login') 
def single(request):

        if request.method== "POST":
               name=request.POST.get('name')
               email=request.POST.get('email')
               message=request.POST.get('message')
               print(name,email,message)
               ins= Comment(name=name ,email=email, message=message)
               ins.save()
               #return HttpResponse("<h1>Thanks For Comment</h1>")
        return render(request, 'main/single.html')

@login_required(login_url='login')     
def blog(request):
        return render(request, 'main/index1.html')
@login_required(login_url='login') 
def shop(request):
        return render(request, 'main/shop.html')
@login_required(login_url='login') 
def reg_form(request):
        return render(request, 'main/reg_form.html')

# implimentation of work start from here----
@login_required(login_url='login') 
def images_get(request):
        data = productimg.objects.all()
        return render (request, 'main/gallery.html', {'data':data})
@login_required(login_url='login') 
def image_get(request):
        data= indeximg.objects.all()
        return render (request, 'main/index1.html', {'data':data})

def image(request):
        data= images.objects.all()
        return render (request, 'main/about1.html', {'data1':data})

        

@login_required(login_url='login') 
def customer(request):
        customer=Customer.objects.all()
        return render(request,'main/typography.html',{'dat':customer}) 

@login_required(login_url='login') 
def savecustomer(request):
        form = addcus()
        if request.method == 'POST':
        #print('Printing POST:',request.POST)
                form = addcus(request.POST)
                if form.is_valid:
                        form.save()
                return redirect('/')
        context ={'form':form}
        return render(request,'main/addcustomer.html',context)
@login_required(login_url='login') 
def edit_data(request, pk):
    form1= Customer.objects.get(id=pk)
    print(form1)
    form= addcus(instance=form1)
    if request.method == 'POST':
        form = addcus(request.POST, instance=form1)
    if form.is_valid():
        form.save()
        return redirect('/customer')
    else:
         form.errors
    context ={'form':form}
    return render(request,'main/addcustomer.html',context)
@login_required(login_url='login') 
def del_customer(request, id):
    f=Customer.objects.get(pk=id)

    f.delete()
    return redirect('/')
        
class index(View):
    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])

        return redirect('/gallery')

#def updatecustomers(request,pk):
        #customer = Customer.objects.get(id=pk)
        
        #if request.method == 'POST':
        #print('Printing POST:',request.POST)
       # fm = addcus(request.POST)
       # if fm.is_valid():
            #form.save()
            #return redirect('/customers')

       # context = {'form':form}
       # return render(request, 'main/addcustomer.html',context)
