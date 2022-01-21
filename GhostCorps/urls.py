from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('LNR_app.urls')),
    path('gb/', include('ghost_app.urls')),
]
