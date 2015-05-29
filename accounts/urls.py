from django.conf.urls import url
from django.contrib.auth import views as authviews
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    url(r'^login/$', authviews.login,
        {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'^logout/$', authviews.logout, {'next_page': '/'}, name='logout'),
    url(r'^password_change/$', authviews.password_change,
        {'template_name': 'accounts/password_change_form.html'},
        name='password_change'),
    url(r'^password_change/done/$', authviews.password_change_done,
        {'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'),
    url(r'^update/', login_required(views.UserUpdate.as_view())),
    url(r'^new/', views.Registration.as_view(), name='registration'),
]
