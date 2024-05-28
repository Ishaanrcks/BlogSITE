"""
URL configuration for blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="login"),
    path("Create/<Blog_Id>",views.Create,name="Create"),
     path("NewBlogs",views.NewBlogs,name="NewBlogs"),
    path("Change",views.Change,name="change"),
    path("MyBlogs",views.UserBlogs,name="MyBlogs"),
    path("LogOut",views.LogOut,name="LogOut"),
     path("Show/<Blog_Id>",views.Show,name="Show"),
     path("Update/<Blog_Id>",views.Update,name="Update"),path("Delete/<Blog_Id>",views.Delete,name="Delete")
     ,path("Favourite/<Blog_Id>",views.Favourite,name="Favourite")
     ,path("YourFavourite",views.YourFavourite,name="YourFavourite")
     ,path("SignUp",views.SignUp,name="SignUp")
     ,path("DoSignUp",views.DoSignUp,name="DoSignUp")
]
