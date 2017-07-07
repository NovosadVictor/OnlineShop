from django.conf.urls import url
from .views import LoginView, RegistrationView, LogoutView, UserView, UsersView


urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', UserView.as_view(), name='user'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^$', UsersView.as_view(), name='users'),
]