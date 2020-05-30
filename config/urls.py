"""opinno URL Configuration

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
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from opinno.apps.starwars.views import (
    HomeView, FilmView, CharacterView, PlanetView, StarshipView, RecentlyVisitedView
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('film/<int:pk>/', FilmView.as_view(), name='film'),
    path('character/<int:pk>/', CharacterView.as_view(), name='character'),
    path('planet/<int:pk>/', PlanetView.as_view(), name='planet'),
    path('starship/<int:pk>/', StarshipView.as_view(), name='starship'),
    path('last-visited/', RecentlyVisitedView.as_view(), name='last-visited')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
