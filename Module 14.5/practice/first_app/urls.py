from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="homepage"),
    path('djangoForm/', views.DjangoForm, name="djangoForm"),
]