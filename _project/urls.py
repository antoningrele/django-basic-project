from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.site.site_header = 'Django Basic Project - Administration'

urlpatterns = [
	url('^', include('django.contrib.auth.urls')),
	url(r'^arriere-boutique/', admin.site.urls, name='admin'),
#	url(r'^phoning/', include('phoning.urls')),
#	url(r'^$', RedirectView.as_view(url="/phoning", permanent=False)),
]