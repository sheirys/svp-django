from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'svp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^auth/', include('django.contrib.auth.urls')),
	url(r'^inventory/', include('inventory.urls')),
	url(r'^plan/', include('plan.urls')),
)

