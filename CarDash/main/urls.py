from django.urls import path
from .views import home_view, config_view, vehicle_selection_view

urlpatterns = [
    path('', home_view, name='home'),
    path('vehicle_selection/', vehicle_selection_view, name='vehicle_selection'),
    path('configuration/', config_view, name='config')
]
