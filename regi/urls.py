from django.conf.urls import patterns, include, url

from regi.regi_test.views import loggedin_view
from regi.regi_test.views import user_creation
from regi.regi_test.views import user_create_success
from regi.regi_test.views import user_activate
from regi.regi_test.views import send_password
from regi.regi_test.views import user_set_password
from regi.regi_test.views import change_password
from regi.news.views import news 
from regi.news.views import news_item

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', loggedin_view),
    (r'^accounts/success/$', user_create_success),
    (r'^accounts/activate/(\w+)/$', user_activate),    
    (r'^accounts/registration/$', user_creation),
    (r'^accounts/sendpassword/$', send_password),
    (r'^accounts/setpassword/(\w+)/$', user_set_password),
    (r'^accounts/changepassword/$', change_password),
    (r'^news/$', news),
    (r'^news/(\d+)/$', news_item),    
    # Examples:
    # url(r'^$', 'regi.views.home', name='home'),
    # url(r'^regi/', include('regi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
