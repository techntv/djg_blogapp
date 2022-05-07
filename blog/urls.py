
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogPostNew, BlogPostEdit, BlogPostDelete

urlpatterns = [
    path('post/<int:pk>/delete/', BlogPostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogPostEdit.as_view(), name='post_edit'),
    path('post/new/', BlogPostNew.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
