from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home, about, contact, blog_list, blog_detail, blog_by_category, blog_by_tag, blog_search


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog_list, name='blog'),
    path("blog/<str:slug>/", blog_detail, name="post"),
    path("blog/category/<str:category>/", blog_by_category, name="category"),
    path("blog/tag/<str:tag>/", blog_by_tag, name="tag"),
    path('search/', blog_search, name='blog_search'),
]