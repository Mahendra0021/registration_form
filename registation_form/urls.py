"""
URL configuration for registation_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage,),
    path('method',views.Home,name='method'),
    path('login/',views.LoginPage,name='login'),
    path('submiti/', views.Home,name='submit'),
    
]





#path('login/', views.LoginPage,name='login'),
    #path('Submit/', views.Home,name='Submit_your_profilee'),
    #path('Submit_your_profile', views.LoginPage,name='Submit_your_profile'),

