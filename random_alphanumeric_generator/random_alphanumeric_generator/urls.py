from django.contrib import admin
from django.urls import path, include

app_name = 'generator_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generator_app.urls', namespace='generator_app')),
]
