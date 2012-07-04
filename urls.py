from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from skarbonka.views import *
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$',common.mainPage),
#	(r'^$',mainPage),
	(r'^jm/$',jm.jmPage),
	(r'^jm/add/$',jm.jmAdd),
	(r'^jm/edit/(\d)/$',jm.jmEdit),
	(r'^jm/edit/$',jm.jmEdit),
	(r'^jm/delete/(\d)/$',jm.jmDel),
	(r'^admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'skarbonka.views.home', name='home'),
    # url(r'^skarbonka/', include('skarbonka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
