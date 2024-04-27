# urls.py in the 'bookstore' app
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',sample,name='sample'),
    path('signup',signup,name='signup'),
    path('home',home,name='home'),
    path('aboutus',aboutus,name='aboutus'),
    path('contactus',contactus,name='contactus'),
    path('books',books,name='books'),
    path('fiction',fiction,name='fiction'),
    path('login',signin,name='login'),
    path('payment',payment,name='payment'),
]
