from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    list_filter = ('user', )
    search_fields = ('user', )

admin.site.register(Profile, ProfileAdmin)
from django.contrib import admin

# Register your models here.
