"""weather/lookup application URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        
    path('about.html', views.about, name='about'),
]
