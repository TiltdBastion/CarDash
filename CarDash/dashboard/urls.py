from django.urls import path
from .views import home_view, config_view

urlpatterns = [
    path('', home_view, name='home'),
    path('configuration/', config_view, name='config')
]
