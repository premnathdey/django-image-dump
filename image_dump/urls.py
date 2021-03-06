"""django_image_dump URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^youtube/', include(('youtube.urls', 'youtube'), namespace='youtube')),
    url(r'^s/', include(('search.urls', 'search'), namespace='search')),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('images.urls', namespace='images')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(
        settings.YOUTUBE_DOWNLOAD_URL, document_root=settings.YOUTUBE_DOWNLOAD_ROOT
    )
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
