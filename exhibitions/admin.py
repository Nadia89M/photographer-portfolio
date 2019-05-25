from django.contrib import admin
from .models import Exhibition

class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id','title')
    search_fields = ('title', )
    list_per_page = 25

admin.site.register(Exhibition, ExhibitionAdmin)
