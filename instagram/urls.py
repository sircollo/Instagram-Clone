from atexit import register
from django.urls import include, path, re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import search_user
urlpatterns = [
    url('$', views.home, name='home'),
    url('^register/',views.register, name='register'),
    url('^home/',views.index, name='index'),
    url('^new_post/',views.postImage, name='upload'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    # url('logout/', views.logout, name='logout'),
    path('search/', search_user.as_view(), name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)