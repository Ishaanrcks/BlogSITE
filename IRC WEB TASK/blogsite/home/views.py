from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth import logout,login,authenticate
from blogdata.models import Blog_data
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.

def index(request):
     if request.user.is_authenticated==True:
         
          return redirect('/NewBlogs')
     
 
     if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user1 = authenticate(username=username, password=password)#Checking the users credential
        
        if user1 is not None:
           #To login User
           login(request, user1)
           curr_user=username
           return redirect('/NewBlogs')
        else:
             return render(request,'login.html',{'UserStatus':"You should Log In first",'message':'FAIL'})

 
     return render(request,'login.html',{'UserStatus':"You should Log In first"})
def Create(request,Blog_Id):
     if request.user.is_authenticated!=True:
         
          return redirect('/')
     elif Blog_Id=='New':
          return render(request,'alter.html',{'date':date.today(),'UserStatus':"Logging Out",'mode':'CREATE'})
     else:
          data=Blog_data.objects.get(Blog_Id=Blog_Id)
          return render(request,'alter.html',{'date':data.Blog_Date,'UserStatus':"Logging Out",'mode':'UPDATE','data':data})

def NewBlogs(request):
     if request.user.is_authenticated!=True:
          
          return redirect('/')
     blogthumbn_data=Blog_data.objects.all().order_by('-Id')
     page=Paginator(blogthumbn_data,3)
     page_num= request.GET.get('page')
     page=page.get_page(page_num)
     total_page=page.paginator.num_pages
     data={'page':page,'heading':'New','UserStatus':"Logging Out",'total_page':total_page,'lst':[n for n in range(1,total_page+1)],'mode':'Show'}
     return render(request,'showblogslist.html',data)
def UserBlogs(request):
     if request.user.is_authenticated!=True:
          
          return redirect('/')
     
     curr_user=''
     curr_user=request.user.username
     
     blogthumbn_data=Blog_data.objects.filter(User_Name=curr_user).order_by('-Id')
   
     page=Paginator(blogthumbn_data,3)
     page_num= request.GET.get('page')
     page=page.get_page(page_num)
     total_page=page.paginator.num_pages
     data={'page':page,'heading':'Your','UserStatus':"Logging Out",'total_page':total_page,'lst':[n for n in range(1,total_page+1)],'mode':'Create'}
     return render(request,'showblogslist.html',data)
     
#Sort of Dummy URL Generated to save and extract form data
def Change(request):
    
        if (request.method=="POST"):
            curr_user=''
            curr_user=request.user.username
            Blogname=request.POST.get('NAME')
            Blogdesc=request.POST.get('DESCRIPTION')
            Blogimg=request.FILES.get('IMAGE')
            en=Blog_data(User_Name=curr_user,Blog_Name=Blogname,Blog=Blogdesc,Blog_Image=Blogimg,Blog_Date=date.today())
            en.save()
        return redirect('/NewBlogs')#here we will redirect the page to blogs tab
        
def LogOut(request):
     if request.user.is_authenticated!=True:
          
          return redirect('/')
     logout(request)
     return redirect('/')

def Show(request,Blog_Id):
     fav_state=0
     curr_user=request.user.username
     curr_user_fav=User.objects.get(username=curr_user).blog_data_set.all()
     curr_blog_name=Blog_data.objects.get(Blog_Id=Blog_Id).Blog_Name
     print(curr_user_fav)
     for i in curr_user_fav:
          if str(i)==str(curr_blog_name):
               fav_state=1
               break
     return render(request,'show.html',{'blog':Blog_data.objects.get(Blog_Id=Blog_Id),'UserStatus':"Logging Out",'state':fav_state})
def Update(request,Blog_Id):
     if (request.method=="POST"):
            Update_obj=Blog_data.objects.get(Blog_Id=Blog_Id)
            Update_obj.Blog_Name=request.POST.get('NAME')
            Update_obj.Blog=request.POST.get('DESCRIPTION')
            if (request.FILES.get('IMAGE')!=None):
                 Update_obj.Blog_Image=request.FILES.get('IMAGE')
                 print(request.POST.get('IMAGE'))
            Update_obj.save()
     return redirect('/NewBlogs')#here we will redirect the page to blogs tab
def Delete(request,Blog_Id):
     print('yashhh')
     Delete=Blog_data.objects.get(Blog_Id=Blog_Id)
     Delete.delete()
     return redirect('/NewBlogs')#here we will redirect the page to blogs tab
def Favourite(request,Blog_Id):
          curr_user=request.user.username
          curr_user_id=User.objects.get(username=curr_user).id
          curr_blog=Blog_data.objects.get(Blog_Id=Blog_Id)
          user_set=curr_blog.Favourite.all()
          status=0
          for i in user_set:
               if str(curr_user)==str(i):
                    status=1
                    break
          if status==0:
               curr_blog.Favourite.add(curr_user_id)
          elif status==1:
               
               curr_blog.Favourite.remove(curr_user_id)
          curr_user_fav=User.objects.get(username=curr_user).blog_data_set.all()
       
          return redirect('Show',Blog_Id)

def YourFavourite(request):
     if request.user.is_authenticated!=True:
          
          return redirect('/')
     curr_user=request.user.username
     blogthumbn_data=User.objects.get(username=curr_user).blog_data_set.all()
     page=Paginator(blogthumbn_data,3)
     page_num= request.GET.get('page')
     page=page.get_page(page_num)
     total_page=page.paginator.num_pages
     data={'page':page,'heading':'Your Favourite','UserStatus':"Logging Out",'total_page':total_page,'lst':[n for n in range(1,total_page+1)],'mode':'Show'}
     return render(request,'showblogslist.html',data)
def SignUp(request):
     data={'mode':'','UserStatus':"You Would be redirected to Login Page"}
     return render(request,'signup.html',data)
def DoSignUp(request):
      if (request.method=="POST"):
            username=request.POST.get('username')
            password=request.POST.get('password')
            cpassword=request.POST.get('confirm password')
            email=request.POST.get('email')
            firstname=request.POST.get('firstname')
            if User.objects.filter(username=username).exists():
               data1={'mode':'Fail','UserStatus':"You Would be redirected to Login Page"}
               return render(request,'signup.html',data1)
            elif( password.isalpha() or password.isdigit() ):
                 data1={'mode':'Fail0','UserStatus':"You Would be redirected to Login Page",'username':username,'email':email,'firstname':firstname}
                 return render(request,'signup.html',data1)
            elif(len(password)<8 ):
                 data1={'mode':'Fail1','UserStatus':"You Would be redirected to Login Page",'username':username,'email':email,'firstname':firstname}
                 return render(request,'signup.html',data1)
            elif(password!=cpassword ):
                 data1={'mode':'Fail2','UserStatus':"You Would be redirected to Login Page",'username':username,'email':email,'firstname':firstname}
                 return render(request,'signup.html',data1)
            else:
                 S_user=User.objects.create_user(username=username,password=password,email=email)
                 S_user.first_name=firstname
                 S_user.save()
                 return redirect('/')
            
        