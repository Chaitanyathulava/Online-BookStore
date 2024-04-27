# views.py in the 'bookstore' app
from django.contrib.auth.models import User
from django.shortcuts import *
from .models import *
from django.contrib.auth import *

def sample(request):
    return render(request,'sample.html')


def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create the user using Django's default User model
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name  # Optionally, set the first name
        user.save()

        return redirect('signup')  # Redirect to some page after successful signup
    return render(request, "register.html")

def signin(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    print(username, password)
    user=authenticate(request, username=username, password = password)
    print(user)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return redirect('signup')
    return render(request,"register.html")


def contactus(request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            textarea = request.POST.get('textarea')
            customer = Feedback.objects.create(name=name, email=email, textarea=textarea)
            customer.save()
            return redirect('contactus')
        return render(request, "contactus.html")

def aboutus(request):
    return render(request,"aboutus.html")

def home(request):
    return render(request,"home.html")

def books(request):
    return render(request,"books.html")

def fiction(request):
    return render(request,"index.html")

def payment(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        nameoncard = request.POST.get('nameoncard')
        creditcardnumber = request.POST.get('creditcardnumber')
        expmonth = request.POST.get('expmonth')
        expyear = request.POST.get('expyear')
        CVV = request.POST.get('CVV')
        sample1 = CheckOut.objects.create(fullname=fullname, email=email, address=address, city=city,state=state,zipcode=zipcode,nameoncard=nameoncard,creditcardnumber=creditcardnumber,expmonth=expmonth,expyear=expyear,CVV=CVV)
        sample1.save()
        return redirect('home')
    return render(request,"payment.html")

