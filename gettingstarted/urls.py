from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    #path("", hello.views.index, name="index"),
    #path("", auth_views.login_required, {'template_name': 'registration/signup.html'}, name='signup'),
    #path("", hello.views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('accounts/logout/', LoginView.as_view(template_name='logout.html'), name='logout'),
    path("", LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("signup/", hello.views.signup, name='signup'),
    path("db/", hello.views.db, name="db"),
    path("text/", hello.views.text, name="text"),
    path("omilia1/", hello.views.omilia1, name="omilia1"),
    path("omilia2/", hello.views.omilia2, name="omilia2"),
    path("omilia3/", hello.views.omilia3, name="omilia3"),
    path("omilia4/", hello.views.omilia4, name="omilia4"),
    path("omilia5/", hello.views.omilia5, name="omilia5"),
    path("omilia6/", hello.views.omilia6, name="omilia6"),
    path("omilia7/", hello.views.omilia7, name="omilia7"),
    path("kyrhgmata/", hello.views.kyrhgmata, name="kyrhgmata"),
    path("contents/", hello.views.contents, name="contents"),
    path("admin/", admin.site.urls),
]
'''
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
'''