from django.conf.urls import patterns, include, url
from django.contrib import admin
from stuff import main

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/users/create$', main.create_user),
    url(r'^api/v1/users/(\d+)$', main.lookup_user),
    url(r'^api/v1/users/(\d+)/update$', main.update_user),
)

