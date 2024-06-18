"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from contact_manager import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_project.urls')),
    path('mpaka-register/', views.MpakaRegisterView.as_view(), name='Mpaka-register'),
    path('mpaka-login/', views.MpakaLoginView.as_view(), name='Mpaka-login'),
    path('mpaka-contacts/', views.MpakaContactListView.as_view(), name='Mpaka-contact-list'),
    path('mpaka-contacts/create/', views.MpakaContactCreateView.as_view(), name='Mpaka-contact-create'),
    path('mpaka-contacts/<int:pk>/update/', views.MpakaContactUpdateView.as_view(), name='Mpaka-contact-update'),
    path('mpaka-contacts/<int:pk>/delete/', views.MpakaContactDeleteView.as_view(), name='Mpaka-contact-delete'),
    path('mpaka-groups/', views.MpakaGroupListView.as_view(), name='Mpaka-group-list'),
    path('mpaka-groups/create/', views.MpakaGroupCreateView.as_view(), name='Mpaka-group-create'),
    path('mpaka-groups/<int:pk>/update/', views.MpakaGroupUpdateView.as_view(), name='Mpaka-group-update'),
    path('mpaka-groups/<int:pk>/delete/', views.MpakaGroupDeleteView.as_view(), name='Mpaka-group-delete'),
]