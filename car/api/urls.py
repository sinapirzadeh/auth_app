from .views import AddCarAPI, ListCarAPI
from django.urls import path



urlpatterns = [
    path('add_car/', AddCarAPI.as_view(), name='add_car'),
    path('show_list/', ListCarAPI.as_view(), name='list_car')
]
