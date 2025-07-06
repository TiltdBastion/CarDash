"""
URL configuration for CarDash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect
def redirect_if_not_auth(request):
    if request.user.is_authenticated:
        return redirect('vehicle_selection')
    else:
        return redirect('login')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_if_not_auth, name='root'),
    path('auth/', include('customauth.urls'), name='login'),
    path('home/', include('main.urls'), name='home'),
]
