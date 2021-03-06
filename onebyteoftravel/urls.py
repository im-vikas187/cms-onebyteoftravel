# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from djangocms_blog.sitemaps import BlogSitemap
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap, 'blog': BlogSitemap,}}),
]

urlpatterns += (
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^(en/)?', include('cms.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots_file")
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
