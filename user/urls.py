from django.urls import path, include
from . import views


urlpatterns = [
    path('user/', include('user.api.urls'))
]
