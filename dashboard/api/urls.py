from .views import ProfileListAPI, ProfileDetailAPI, MyProfileAPI
from django.urls import path, include

urlpatterns = [
    path('profile/<int:id>/', ProfileDetailAPI.as_view(), name='profile_detail'),
    path('profiles_show/', ProfileListAPI.as_view(), name='profile_list'),
    path('my_info/', MyProfileAPI.as_view(), name='my_profile')
]
