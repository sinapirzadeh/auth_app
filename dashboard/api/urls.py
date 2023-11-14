from .views import ProfileListAPI, ProfileDetailAPI, MyProfileAPI
from django.urls import path, include

urlpatterns = [
    path('my_info/', MyProfileAPI.as_view(), name='my_profile'),
    path('profiles_show/', ProfileListAPI.as_view(), name='profile_list'),
    path('profile/<int:pk>/', ProfileDetailAPI.as_view(), name='profile_detail'),
]
