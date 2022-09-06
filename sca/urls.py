from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('aplic.urls')),
    path('restrito/', admin.site.urls),

]
