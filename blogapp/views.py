from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import PostModel,Comment,Contact
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    posts=PostModel.objects.all().order_by('-id')
    return render(request,'blogapp/homepage.html',{"posts":posts})
    


def single_post(request, id):
    post=PostModel.objects.get(id=id)
    comments=Comment.objects.filter(post=post).order_by('-id')
    context={
        'comments':comments,
        'post':post
        }
    return render(request,'blogapp/singlepage.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('first_name')
        email=request.POST.get('email')
        ph_no=request.POST.get('phone')
        text=request.POST.get('comment')
        obj=Contact(name=name,email=email,ph_no=ph_no,text=text)
        obj.save()
    return render(request,'blogapp/contact.html')
  
@login_required
@require_http_methods(["POST"])
def add_comment(request,post_id):
    post_obj=PostModel.objects.get(id=post_id)
    comment_obj=Comment(post=post_obj,owner=request.user,comment_body=request.POST["msg"])
    comment_obj.save()
    return HttpResponseRedirect(reverse("blogapp:single_post",args=(post_id,)))

@require_http_methods(["POST","GET"])
def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if not username or not password:
            return render(request,'blogapp/login.html',{"msg":"Both user name & password require to login"})
        else:
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse("blogapp:homepage"))
            else:
                return render(request,'blogapp/login.html',{"msg":"Invalid user & password"})
        
    elif request.method=="GET":
        msg=request.GET.get("msg")
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('blogapp:homepage'))
        return render(request,'blogapp/login.html',{"msg":msg})

        
@require_http_methods(["GET","POST"])
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password_confrim=request.POST.get('password_confrim')
        if not username or not email or not password or not password_confrim:
            return render(request,'blogapp/signup.html',{"msg":"All fields are mandotary"})
        elif password!=password_confrim:
            return render(request,'blogapp/signup.html',{"msg":"Password & confrom password is not matching"})
        elif User.objects.filter(username=username).exists():
            return render(request,'blogapp/signup.html',{"msg":"Username already exists,Please use different user name."})
        elif User.objects.filter(email=email).exists():
            return render(request,'blogapp/signup.html',{"msg":"Email already exists,Please use different user Email."})  
        else:
            user=User.objects.create_user(username,email,password)
            return HttpResponseRedirect(reverse("blogapp:login_user") + "?msg=User created Succesfully. Please login")
    else:
        return render(request,'blogapp/signup.html',{})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("blogapp:login_user"))


def about(request):
    return render(request,'blogapp/about.html')

