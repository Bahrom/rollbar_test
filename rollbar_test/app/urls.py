from django.urls import path

from . import views

urlpatterns = [
    path('', views.info, name='index'),
    path('error/', views.error, name='error'),
    path('warning/', views.warning, name='warning'),
    path('critical/', views.critical, name='critical'),

]