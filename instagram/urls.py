from atexit import register
from django.urls import include, path, re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('$', views.home, name='home'),
    url('^register/',views.register, name='register'),
    
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)