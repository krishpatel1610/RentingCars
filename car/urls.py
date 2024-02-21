from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "kathan shah"
admin.site.site_title = "welcome to dashbord"
admin.site.index_title = "welcome to index dashbord"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myapp.urls")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)