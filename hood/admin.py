from hood.models import Authorities, BlogPost, Business, Health, Profile, healthservices, neighbourhood, notifications
from django.contrib import admin

# Register your models here.
admin.site.register(Profile);
admin.site.register(neighbourhood);
admin.site.register(BlogPost);
admin.site.register(Business);
admin.site.register(Health);
admin.site.register(healthservices);
admin.site.register(Authorities);
admin.site.register(notifications);