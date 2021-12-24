from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.views import View

urlpatterns = [
    path('',index, name='index'),
    path('register',register, name='register'),
    path('login',NewLogin.as_view(), name='login'),
    path('add',add, name='add'),
    path('show',show, name='show'),
    path('edit',edit, name='edit'),
    path('delete',delete, name='delete'),
]






if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)