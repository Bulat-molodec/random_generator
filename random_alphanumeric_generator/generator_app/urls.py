from django.urls import path
from . import views

app_name = 'generator_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate, name='generate'),
]
