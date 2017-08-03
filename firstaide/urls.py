from django.conf.urls import url
from .views import *

urlpatterns = [
		url(r'^$',
        ListFirstAideAPIView.as_view(),
        name = 'first_aide_api_home'),

		url(r'^create/$',
        CreateFirstAideAPIView.as_view(),
        name='first_aide_api_create'),

        url(r'^delete_post/(?P<pk>\d+)$',
        DeleteFirstAideAPIView.as_view(),
        name='first_aide_api_delete_post'),

	    url(r'^edit_post/(?P<pk>\d+)$',
        UpdateFirstAideAPIView.as_view(),
        name='first_aide_api_edit_post'),

	    url(r'^view_post/(?P<pk>\d+)$',
        ViewFirstAideAPIView.as_view(),
        name='first_aide_api_view_post'),

]
