from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',)

def authorities(request):
    return render(request,'authorities/authorities.html',)


def new_blogpost(request):
    return render(request,'blog/blogpost_form.html',)

def blog(request):
    return render(request,'blog/blogs.html',)


def view_blog(request):
    return render(request,'blog/view_blog.html',)




