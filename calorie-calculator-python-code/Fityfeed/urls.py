from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('user/',views.userPage,name='userPage'), #userPage
    path('product/',views.fooditem,name='fooditem'),
    path('createfooditem/',views.createfooditem,name='createfooditem'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('addFooditem/',views.addFooditem,name='addFooditem'),
    path('user/About.html',views.about,name='about'), #about us page
    path('user/feedback.html',views.feedback,name='feedback'), #feedback form
    path('user/contactus.html',views.contact,name='contact'), #contact us page
    path('user/user.html',views.userPage,name='userPage'), #userPage
    
]
