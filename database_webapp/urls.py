"""database_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from scientific_database_app import views
from django.conf.urls import url, include
from django.views.generic.base import TemplateView

urlpatterns = [
    #path("", views.home, name="home")
    path('admin/', admin.site.urls),
#    url('scientific_database_app/home/', TemplateView.as_view(template_name='site.html'), name='home'),
#    path('scientific_database_app/', include('django.contrib.auth.urls'), name='scientific_database_app'),
#    url('scientific_database_app/device_registration/', views.device_registration, name='device_registration'),
#    url('scientific_database_app/device-list/', views.RegDevices, name='device-list'),
#    url('scientific_database_app/maintenance/', views.AddMaintenance, name='Maintenance'),
#    url('scientific_database_app/maintenance-list/', views.MaintenanceList, name='maintenance-list'),
#    url(r'^scientific_database_app/maintenance-detail/(?P<id>\d+)/$', views.MaintenanceDetail, name='maintenance-detail'),

#path('scientific_database_app/', include('django.contrib.auth.urls'), name='scientific_database_app'),
    path('scientific_database_app/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='site.html'), name='home'),
    path('device_registration/', views.device_registration, name='device_registration'),
    path('device-list/', views.RegDevices, name='device-list'),
    path('maintenance/', views.AddMaintenance, name='maintenance'),
    path('measurement/', views.AddMeasurement, name='measurement'),
    path('maintenance-list/', views.MaintenanceList, name='maintenance-list'),
    path(r'^maintenance-detail/(?P<id>\d+)/$', views.MaintenanceDetail, name='maintenance-detail'),
    path('account/', include('django.contrib.auth.urls'), name='user_login'),
    path('ajax/load-associated-devices/', views.load_associated_devices, name='ajax_load_associated_devices'),

]
