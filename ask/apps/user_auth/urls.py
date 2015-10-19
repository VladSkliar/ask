from django.conf.urls import patterns, url
from user_auth import views

urlpatterns = patterns(
  'user_auth.views',
  url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
  url(r'^login/$', 'login_view', name='login'),
  url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
  url(r'^$', 'index', name='index'),
)
