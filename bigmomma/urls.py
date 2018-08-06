from django.contrib import admin
from django.urls import path, include
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
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)