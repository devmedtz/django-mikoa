from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mikoa/', include('mikoa.urls', namespace='mikoa')),
    path('example/', include('example.urls', namespace='example')),
]
