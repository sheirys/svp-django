from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'svp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^auth/login/$', 'django.contrib.auth.views.login'),
	url(r'^auth/logout/$', 'django.contrib.auth.views.logout'),
)

