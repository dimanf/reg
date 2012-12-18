from django.conf.urls import patterns, include, url

from regi.regi_test.views import get_user_name

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^reg/', get_user_name),
    # Examples:
    # url(r'^$', 'regi.views.home', name='home'),
    # url(r'^regi/', include('regi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
