from django.conf.urls import patterns, include, url
from django.contrib import admin
from stuff import main

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', main.start),
)

