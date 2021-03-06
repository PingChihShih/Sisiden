"""SiSiDen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import login
from main.views import order
from main.views import check
from main.views import result
from main.views import manage, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', order, name='index'),
    path('delete', delete, name='delete'),
    path('login', login, name='login'),
    path('order', order, name='order'),
    path('check', check, name='check'),
    path('result', result, name='result'),
    path('manage', manage, name='manage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
