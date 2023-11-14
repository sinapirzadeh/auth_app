from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_page/', include('user.urls')),
    path('car_page/', include('car.urls')),
    path('dashboard_page/', include('dashboard.urls'))
]
