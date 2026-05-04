from django.urls import include, path

from apps.blog.api import CategoryListAPIView, PostDetailAPIView, PostListAPIView
from apps.blog.feeds import AtomLatestPostsFeed, LatestPostsFeed
from apps.blog.views import (
    AuthorPostListView,
    BlogPostReviewView,
    CategoryPostListView,
    ContentsListView,
    HomeView,
    IndexListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView,
    SearchResultsView,
    SearchView,
)


app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "user/<str:username>/posts", AuthorPostListView.as_view(), name="author_posts"
    ),
    path(
        "category/<slug:slug>/posts",
        CategoryPostListView.as_view(),
        name="category_posts",
    ),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("review/", BlogPostReviewView.as_view(), name="blog_review"),
    path("post/<slug:slug>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("search/", SearchView.as_view(), name="search"),
    path("search/results/", SearchResultsView.as_view(), name="search_results"),
    path("index/", IndexListView.as_view(), name="index"),
    path("contents/", ContentsListView.as_view(), name="contents"),
    path("sitenews/rss/", LatestPostsFeed(), name="post_feed"),
    path("sitenews/atom/", AtomLatestPostsFeed(), name="post_feed"),
    path("users/", include("apps.account.urls", namespace="users")),
    # API
    path("api-auth/", include("rest_framework.urls")),
    path("api/posts/", PostListAPIView.as_view(), name="api_posts"),
    path("api/posts/<int:pk>/", PostDetailAPIView.as_view(), name="api_post_detail"),
    path("api/categories/", CategoryListAPIView.as_view(), name="api_blog_categories"),
]
