from django.urls import path

from .import views

app_name = "example"

urlpatterns = [
    path('application/', views.application, name='application'),
    path('ajax-load-districts/', views.ajax_load_districts, name='ajax_load_districts'),
]