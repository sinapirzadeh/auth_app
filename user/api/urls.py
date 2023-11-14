from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.SignUpAPI.as_view(), name='signup'),
    path('login/', views.LogInAPI.as_view(), name='login'),
]
