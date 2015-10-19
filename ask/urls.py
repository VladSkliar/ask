from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.question import views


urlpatterns = patterns(
  'user_auth.views',
  url(r'^user/', include('user_auth.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^question/', include('question.urls')),
  url(r'^user_list/', views.UserListView.as_view(), name='user_list'),
  url(r'^$', 'index', name='index'),
)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
