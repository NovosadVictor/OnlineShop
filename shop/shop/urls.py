from django.conf.urls import url
from .views import ProductsView, ProductDetailView, CategoriesView


urlpatterns = [
    url(r'^categories/$', CategoriesView.as_view(), name='categories'),
    url(r'^products/$', ProductsView.as_view(), name='products'),
    url(r'^(?P<category>[0-9]+)/products/$',
        ProductsView.as_view(), name='category_products'),
    url(r'^(?P<category>[0-9]+)/(?P<slug>[-\w]+)/$',
        ProductDetailView.as_view(), name='product_detail'),
]