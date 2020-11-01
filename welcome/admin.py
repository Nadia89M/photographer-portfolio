from django.contrib import admin
from .models import Welcome


class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25


admin.site.register(Welcome, WelcomeAdmin)

# Register your models here.
