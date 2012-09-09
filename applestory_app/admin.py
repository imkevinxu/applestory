from applestory_app.models import *
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'displayname', 'created_at')
    list_filter = ('created_at',)
    ordering = ['-created_at']
    search_fields = ['user', 'displayname']

admin.site.register(UserProfile, UserProfileAdmin)