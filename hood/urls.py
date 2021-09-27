
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
    url(r'^buznesses',views.buznesses, name='buzness'),
    url(r'^new/business$',views.new_business, name='new-business'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)