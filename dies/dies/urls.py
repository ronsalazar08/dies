from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve


from . import views

admin.site.site_header = 'Torres Technology Center Corporation'
admin.site.site_title = "T-TECH|Dies"
admin.site.index_title = "Welcome to T-TECH Crimping Dies Page"
admin.site.enable_nav_sidebar = False


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('shutdown/', views.shutdown, name='shutdown'),
    path('supermarket/', include('super_market.urls')),
    path('sparemarket/', include('spare_market.urls')),
    path('inventory/', include('inventory.urls')),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                             document_root=settings.MEDIA_ROOT)