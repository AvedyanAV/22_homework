from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, MyModelDeletView, BlogUpdateView

app_name = 'blog'

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_form/', BlogCreateView.as_view(), name='blog_form'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_delete/<int:pk>/', MyModelDeletView.as_view(), name='blog_delete'),
]