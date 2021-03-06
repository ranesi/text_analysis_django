"""text_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from ta_web import views

urlpatterns = [
    #####################################
    # ADMIN CONSOLE
    #####################################
    url(
        r'^admin/',
        admin.site.urls
    ),
    #####################################
    # ta_web
    #####################################
    # route to ta_web
    url(
        r'^',
        include(
            'ta_web.urls',
            namespace='ta_web'
        )
    ),
    # login
    url(
        r'^accounts/login/',
        auth_views.login,
        name='login'
    ),
    # logout
    url(
        r'^accounts/logout/$',
        auth_views.logout,
        name='logout'
    ),
    # register
    url(
        r'^register/$',
        views.register,
        name='register'
    ),
]
