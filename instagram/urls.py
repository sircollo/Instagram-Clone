from atexit import register
from django.urls import include, path, re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import search_user
from .views import CreateProfilePageView
urlpatterns = [
    url('$', views.home, name='home'),
    url('^register/',views.register, name='register'),
    url('^home/',views.index, name='index'),
    url('^new_post/',views.postImage, name='upload'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url('^profile/(\d+)', views.profile, name='profile'),
    # url('logout/', views.logout, name='logout'),
    path('search/', search_user.as_view(), name='search'),
    path('comments/<str:pk>', views.comments, name='comments'),
    path('update_profile/<str:id>', views.updateProfile, name='update_profile'),
    path('follow/<str:pk>', views.follow, name='follow'),
    path('unfollow/<str:pk>', views.follow, name='unfollow'),
    path('like/<str:pk>', views.like, name='likes'),
    path('create_profile/',CreateProfilePageView.as_view(), name='create_profile_page'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)