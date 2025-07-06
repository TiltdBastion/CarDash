from django.urls import path
from .views import dashboard_view, config_view, vehicle_selection_view

urlpatterns = [
    path('vehicle_selection/', vehicle_selection_view, name='vehicle_selection'),
    path('dashboard/<int:car_id>/', dashboard_view, name='dashboard'),
    path('configuration/<int:car_id>/', config_view, name='config')
]
