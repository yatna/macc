from django.conf.urls import include, url
from rest_framework import routers

from malaria_api import views as malaria_api_views
from pcsa import views as pcsa_views
from pcsa_GHN import views as ghn_views
from pcsa_safety_tools import views as safetytools_views
from profiles import views as profiles_views
from signup import views as signup_views
from webhub import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pcsa_posts', pcsa_views.PcsaPostViewSet)
router.register(r'malaria_posts', malaria_api_views.PostViewSet)
router.register(r'malaria_users', malaria_api_views.MalariaUsersViewSet)
router.register(r'gethelpnow/posts', ghn_views.ghnPostsViewSet)
router.register(r'gethelpnow/contacts', ghn_views.ContactViewSet)
router.register(r'safetytools/posts', safetytools_views.SafetyToolsPostViewSet)

urlpatterns = [
    url(r'^index/$',
        views.index,
        name='index'),
    url(r'^$',
        views.dashboard,
        name='dashboard'),
    url(r'^signup_page/$',
        signup_views.signup_page,
        name='signup_page'),
    url(r'^signup_do/$',
        signup_views.signup_do,
        name='signup_do'),
    url(r'^send_verification_email/$',
        signup_views.send_verification_email,
        name='send_verification_email'),
    url(r'^send_email/$',
        signup_views.send_email,
        name='send_email'),
    url(r'^login_do/$',
        profiles_views.login_do,
        name='login_do'),
    url(r'^logout_do/$',
        profiles_views.logout_do,
        name='logout_do'),
    url(r'^profile/$',
        profiles_views.profile,
        name='profile'),
    url(r'^edit_profile/$',
        profiles_views.edit_profile,
        name='edit_profile'),
    url(r'^edit_profile_page/$',
        profiles_views.edit_profile_page,
        name='edit_profile_page'),
    url(r'^forgot_pass_page/$',
        profiles_views.forgot_pass_page,
        name='forgot_pass_page'),
    url(r'^forgot_pass/$',
        profiles_views.forgot_pass,
        name='forgot_pass'),
    url(r'^verify/$',
        signup_views.verify,
        name='verify'),
    url(r'^reset_pass_page/$',
        profiles_views.reset_pass_page,
        name='reset_pass_page'),
    url(r'^change_pass/$',
        profiles_views.change_pass,
        name='change_pass'),
    url(r'^change_pass_page/$',
        profiles_views.change_pass_page,
        name='change_pass_page'),
    url(r'^pcuser/$',
        views.pcuser_list,
        name='pcuser_list'),
    url(r'^pcuser/(?P<pk>[0-9]+)/$',
        views.pcuser_detail,
        name='pcuser_detail'),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')),
    url(r'^api/',
        include(router.urls)),
    url(r'^aboutPC/$',
        views.aboutPC,
        name='aboutPC'),
    url(r'^policies/$',
        views.policies,
        name='policies'),
    url(r'^details/$',
        views.details,
        name='details'),
    url(r'^helpPC/$',
        views.helpPC,
        name='helpPC'),
    url(r'^login_real/$', views.login_real, name = 'login_real'),
    url(r'^login_social/$', views.login_social, name = 'login_social'),
]
