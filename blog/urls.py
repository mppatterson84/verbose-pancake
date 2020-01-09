from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    PostListAllView,
    PostSearchView,
    CategoryListView,
    CategoryFilterView,
)

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/new/', PostCreateView.as_view(), name='post-new'),
    path('blog/<int:pk>/<slug:slug>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('blog/<int:pk>/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('blog/search/', PostSearchView.as_view(), name='blog-search'),
    path('blog/all/', PostListAllView.as_view(), name='post-list-all'),
    path('blog/categories/', CategoryListView.as_view(), name='category-list'),
    path('blog/categories/filter/', CategoryFilterView.as_view(), name='category-filter'),
]