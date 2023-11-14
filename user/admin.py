from django.contrib import admin
from .models import CustomUser

# Register your models here.


admin.site.register(CustomUser)

# @admin.register(MyUserManager)
# class MyUserManagerAdmin(admin.ModelAdmin):
#     pass
