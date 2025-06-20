from django.urls import path
from . import views

app_name = 'fbi_serial_killer'

urlpatterns = [
    path('captures/', views.capture_list, name='capture_list'),
]