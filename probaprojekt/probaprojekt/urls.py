from django.contrib import admin
from django.urls import path
from probaapp.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proba/', home_view, name='home'),
    ]
