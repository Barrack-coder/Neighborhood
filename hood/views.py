from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *


# Create your views here.

def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
    return render(request,'index.html',)


def authorities(request):
    return render(request,'authorities/authorities.html',)


def new_blogpost(request):
    return render(request,'blog/blogpost_form.html',)

def blog(request):
    return render(request,'blog/blogs.html',)


def view_blog(request):
    return render(request,'blog/view_blog.html',)



def biznesses(request):
    return render(request,'business/biznesses.html',)


def new_business(request):
    return render(request,'business/business_form.html',)



def search_results(request):
        return render(request,'business/search.html',)
    
    
def health(request):
    return render(request,'health/health.html',)


def notification(request):
    return render(request,'notifications/notification.html',)


def new_notification(request):
    return render(request,'notifications/notification_form.html',)



def my_profile(request):
    return render(request,'profile/user_profile.html',)



def update_profile(request):
    return render(request,'profile/update_profile.html',)


def user_profile(request):
   return render(request,'profile/user_profile.html',)


def login(request):
   return render(request,'registration/login.html',)



def registration_form(request):
   return render(request,'registration/registration_form.html',)











