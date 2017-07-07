from django.conf.urls import url
from .views import OrderView


urlpatterns = [
    url(r'^$', OrderView.as_view(), name='order'),
]