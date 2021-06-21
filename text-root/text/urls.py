from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('reversed/', views.reverse, name='reverse'),
    path('special/', views.special, name='special'),
]