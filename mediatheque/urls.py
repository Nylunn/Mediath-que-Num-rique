"""
URL configuration for mediatheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from media import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listelivres),
    path('ajoutlivre/', views.ajoutlivre),
    path('updatelivre/<int:id>/', views.updatelivre),
    path('deletelivre/<int:id>/', views.deletelivre),
    path('ajoutcd/', views.ajoutCd),
    path('updatecd/<int:id>/', views.updatecd),
    path('deletecd/<int:id>/', views.deletecd),
    path('ajoutdvd/', views.ajoutDvd),
    path('updatedvd/<int:id>/', views.updatedvd),
    path('deletedvd/<int:id>/', views.deletedvd),
    path('ajoutplateau/', views.ajoutPlateau),
    path('ajoutEmprunter/', views.ajoutEmprunteur),
    #    path('updatemembre/', views.updateEmprunteur)
]
