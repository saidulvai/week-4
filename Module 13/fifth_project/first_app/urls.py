from django.urls import path, include

from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('submitForm/', views.submitForm, name='submitForm'),
    path('django_form/', views.PasswordValidation, name='django_form'),
]