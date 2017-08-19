from django.conf.urls import url

from malaria_web import views
from malaria_web.views import ListPostView, CreatePostView, UpdatePostView, DeletePostView, ViewPostView, ListAppUsersView

# Connect URLs to Views here
urlpatterns = [
    url(r'^create_post/$', 
    	CreatePostView.as_view(), 
    	name='create_post'),

    #(?P<pk>\d+ explained -
        #In Python regular expressions, the syntax for named regular-expression groups is 
        #(?P<name>pattern), where name is the name of the group and pattern is some pattern to match.
        # Here pattern is d+ (decimal digits 1 or more eg 0, 11 , 463). Hence, ?P<pk>5 will render value of pk as 5 

    url(r'^delete_post/(?P<pk>\d+)$', 
    	DeletePostView.as_view(), 
    	name='delete_post'),

    url(r'^edit_post/(?P<pk>\d+)$', 
    	UpdatePostView.as_view(), 
    	name='edit_post'),

    url(r'^list_posts/$', 
    	ListPostView.as_view(), 
    	name='list_posts'),

    url(r'^view_post/(?P<pk>\d+)$', 
    	ViewPostView.as_view(), 
    	name='view_post'),

    url(r'^list_app_users/$', 
        ListAppUsersView.as_view(), 
        name='list_users'),
]
