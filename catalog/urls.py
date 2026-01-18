from django.urls import path
from .views import ProductDetailView, ProductListView, ProductTemplateView

app_name = 'catalog'

urlpatterns = [
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),

]
