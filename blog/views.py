from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUp_form, BlogPost_form, LoginIn_form
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import BlogPost_table
from django.core.cache import cache
from django.db.models import Q



def home(request):
    print('View Called')
    posts=BlogPost_table.objects.all()
    return render(request,'blog/home.html',{'blogposts':posts})

def about(request):
    print('View Called')
    return render(request,'blog/about.html')

def contact(request):
    print('View Called')
    return render(request,'blog/contact.html')


def user_signup(request):
    print('View Called')
    if request.method == "POST":
        form = SignUp_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'user signed up successfully')
            # return HttpResponseRedirect('/blog/dashboard/')
    else:
        form=SignUp_form()
    return render(request,'blog/signup.html',{'signupform':form})


def user_login(request):
    print('View Called')
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginIn_form(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                autheduser = authenticate(username = uname, password = upass)
                if autheduser != None:
                    login(request,autheduser)
                    messages.success(request,' !! Logged in successfully !!')
                    return HttpResponseRedirect('/blog/dashboard/')
        else:
            form = LoginIn_form()
        return render(request,'blog/login.html',{'loginform':form})
    else:
        return HttpResponseRedirect('/blog/dashboard/')


def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogPost_form(request.POST)
            if form.is_valid():
                tit = form.cleaned_data['title']
                desc = form.cleaned_data['description']
                na = BlogPost_table(title=tit,description=desc,user=request.user)
                na.save()
                form = BlogPost_form()
                posts = BlogPost_table.objects.filter(Q(user__username=request.user))
                messages.success(request,'!!! blog successfully posted !!!')
        else:
            form = BlogPost_form()
            posts = BlogPost_table.objects.filter(Q(user__username=request.user))
            print(request.user)
            print(posts)
            # cookie = request.session.get('ip',default= 'No ID')
            # logincount = cache.get('count',version = request.user.id)
        return render(request,'blog/dashboard.html',{'postform':form,'blogs':posts})


def user_logout(request):
    print('View Called')
    logout(request)
    return HttpResponseRedirect('/')



def edit_post(request,postid):
    print('View Called')
    if request.user.is_authenticated:
        if request.method == "POST":
            target = BlogPost_table.objects.get(pk=postid)
            form = BlogPost_form(request.POST, instance=target)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/blog/dashboard/')
        else:
            target = BlogPost_table.objects.get(pk=postid)
            form = BlogPost_form(instance=target)
        return render(request,"blog/editpost.html",{'editform':form})



def delete_post(request,postid):
    print('View Called')
    if request.user.is_authenticated:
        target = BlogPost_table.objects.get(pk=postid)
        target.delete()
        return HttpResponseRedirect('/blog/dashboard/')