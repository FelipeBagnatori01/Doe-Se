from django.urls import path
from . import views
from .views import search_results

urlpatterns = [
    path('feed/', views.show_feed, name="show_feed"),
    path('feed_org/', views.show_feed_org, name="show_feed_org"),
    path('create/', views.create_post, name="create_post"),
    path('organization/', views.show_feed_org, name="show_feed_org"),
    path('config/', views.config, name="config"),
    path('profile/<str:user_id>', views.profile, name="profile"),
    path('profile_org/<str:user_id>', views.profile_org, name="profile_org"),
    path('', views.landing, name="landing"),
    path('institution_created/', views.institutes, name="institution_created"),
    path('user_logged/', views.user_login, name="user_logged"),
    path('institution_logged/', views.institution_login, name="institution_logged"),
    path('upload/', views.upload, name="upload"),
    path('search/', views.search_results, name="search"),
    path('like/<int:post_id>', views.like_postSF, name="like_postSF"),
    path('like_org/<int:post_id>', views.like_postSFO, name="like_postSFO")
]
