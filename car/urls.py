from django.urls import path, include

urlpatterns = [
    path('car/', include('car.api.urls')),
]
