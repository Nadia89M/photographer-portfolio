from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('tearsheets/', include('tearsheets.urls')),
    path('works/', include('works.urls')),
    path('recent_activities/', include('activities.urls')),
    path('elements/', include('posts.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('exhibitions/', include('exhibitions.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
