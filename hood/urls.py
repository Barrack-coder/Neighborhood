
from django.conf.urls import url
from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='Index'),
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
    path('user/',views.user_profile,name='user-profile'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)