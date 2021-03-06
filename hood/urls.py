
from django.conf.urls import url
from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.index,name='index'),
    url(r'^authorities',views.authorities, name='authorities'),
    url(r'^blog',views.blog, name='blog'),
    url(r'^new/blogpost$',views.new_blogpost, name='new-blogpost'), 
    path('view/blog',views.view_blog,name='view_blog'),
    url(r'^biznesses',views.biznesses, name='bizness'),
    url(r'^new/business$',views.new_business, name='new-business'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^health',views.health, name='health'),
    url(r'^notifications',views.notification, name='notification'),
    url(r'^new/notification$',views.new_notification, name='new-notification'),
    url(r'^my-profile/',views.my_profile, name='my-profile'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    path('user/',views.user_profile,name='user-profile'),
    path('register',views.registration_form,name='registration_form'),
    path('login',views.login,name='login'),
    path('logout',views.signout,name='logout'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)