"""flickr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('gallery.api.base.urls')),
    url(r'^api/v1/', include('external_data_sources.api.base.urls')),
    url(r'^api/v1/login$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^login/refresh$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^login/verify$', TokenVerifyView.as_view(), name='token_verify'),
]
