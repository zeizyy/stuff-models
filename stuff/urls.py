from django.conf.urls import patterns, include, url
from stuff import main

urlpatterns = patterns('',
                       url(r'^api/v1/users/create$', main.create_user),
                       url(r'^api/v1/users/(\d+)$', main.lookup_user),
                       url(r'^api/v1/users/(\d+)/update$', main.update_user),
                       url(r'^api/v1/users/recent_givers$', main.recent_givers),

                       url(r'^api/v1/things/leave$', main.leave_thing),
                       url(r'^api/v1/things/(\d+)$', main.lookup_thing),
                       url(r'^api/v1/things/(\d+)/take$', main.take_thing),
                       url(r'^api/v1/things/recent$', main.recent_things),
                       
)

