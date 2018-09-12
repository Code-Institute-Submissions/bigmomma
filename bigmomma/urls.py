from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as authViews
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', include('shop.urls')),
    path('search/', include('search.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('accounts/create/', views.signupView, name='signup'),
    path('accounts/login/', views.signinView, name='signin'),
    path('accounts/logout/', views.signoutView, name='signout'),
    re_path(r'^account/password_reset/$', authViews.password_reset, {'template_name' : 'accounts/reset_password.html' }, name='password_reset'),
    re_path(r'^account/password_reset/done/$', authViews.password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
    re_path(r'^account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', authViews.password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html'}, name='password_reset_confirm'),
    re_path(r'^account/reset/done/$', authViews.password_reset_complete, {'template_name': 'accounts/reset_done.html'}, name='password_reset_complete'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)