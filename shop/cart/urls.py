from django.conf.urls import url
from .views import UserCartView, AddView, DeleteView, ClearView


urlpatterns = [
    url(r'^$', UserCartView.as_view(), name='cart'),
    url(r'^add/$', AddView.as_view(), name='add'),
    url(r'^delete/$', DeleteView.as_view(), name='delete'),
    url(r'^clear/$', ClearView.as_view(), name='clear'),
]