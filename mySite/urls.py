"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from myApp import views as v

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'home', v.home, name='home'),
    url(r'sports',v.sports, name= 'sports'),
    url(r'politics',v.politics, name= 'politics'),
    url(r'business',v.business, name= 'business'),
    url(r'signin',v.signin, name= 'signin'),
    url(r'makeAccount',v.makeAccount, name= 'makeAccount'),
    url(r'profile',v.profile, name= 'profile')

]
