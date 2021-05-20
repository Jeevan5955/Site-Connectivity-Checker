from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^status/', views.status, name='status'),
    url(r'^multiple/', views.multiple, name='multiple'),
    path('^delete/<str:pk>', views.urldeleteform, name='urldeleteform'),
]
