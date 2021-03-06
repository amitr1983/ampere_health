from django.conf.urls import url

from . import views

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
	# url(r'^$', views.index, name='fitbit-home'),
    url(r'^login/$', views.login, name='fitbit-login'),
    url(r'^complete/$', views.complete, name='fitbit-complete'),
    url(r'^error/$', views.error, name='fitbit-error'),
    url(r'^logout/$', views.logout, name='fitbit-logout'),
	url(r'^register/$', views.register, name='app-register'),
	url(r'^home/$', views.home, name='app-home'),
	url(r'^logout/$', views.logout_page, name='app-logout'),
	url(r'^register/success/$', views.register_success, name='app-success'),
     # Fitbit data retrieval
	url(r'^get_data/(?P<category>[\w]+)/(?P<resource>[/\w]+)/$',
		views.get_data, name='fitbit-data'),
	url(r'^get_steps/$', views.get_steps, name='fitbit-steps')
]
