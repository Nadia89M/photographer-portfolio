from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id','title')
    search_fields = ('title', )
    list_per_page = 25

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("slug", )
        form = super(ActivityAdmin, self).get_form(request, obj, **kwargs)
        return form

admin.site.register(Activity, ActivityAdmin)
