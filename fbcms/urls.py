"""fbcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import UserViewset, Logout, MyObtainTokenPairView, RegisterApi, ChangePasswordView, UpdateUserView
from member.views import FollowUpViewset, NotesViewset, CalendarViewset, EventViewset, OccurenceViewset, IndexViewset


router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'follow-up', FollowUpViewset)
router.register(r'notes', NotesViewset)
router.register(r'calendar', CalendarViewset)
router.register(r'event', EventViewset)
router.register(r'occurence', OccurenceViewset)
urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', IndexViewset.as_view(), name="index"),
    # path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/logout/', Logout.as_view(), name='token_destroy'),
    # path('api/registeration/', RegisterApi.as_view()),
    # path('api/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    # path('api/update_profile/<int:pk>/', UpdateUserView.as_view(), name='auth_update_profile'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)