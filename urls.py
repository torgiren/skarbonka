from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from skarbonka.views import *
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$',mainPage),
	(r'^jm/$',jmPage),
	(r'^jm/add/$',jmAdd),
	(r'^jm/edit/(\d)/$',jmEdit),
	(r'^jm/edit/$',jmEdit),
	(r'^jm/delete/(\d)/$',jmDel),
	(r'^admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'skarbonka.views.home', name='home'),
    # url(r'^skarbonka/', include('skarbonka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
