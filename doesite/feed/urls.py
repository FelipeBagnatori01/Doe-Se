from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.show_feed, name="show_feed"),
    path('feed_org/', views.show_feed_org, name="show_feed_org"),
    path('create/', views.create_post, name="create_post"),
    path('organization/', views.show_feed_org, name="show_feed_org"),
    path('config/', views.config, name="config"),
    path('login/', views.login, name="login"),
    path('', views.landing, name="landing"),
    path('create_account/', views.create_account, name="create_account"),
    path('create_institution/', views.create_institution, name="create_institution"),
    path('profile/', views.profile, name="profile"),
    path('profile_org/', views.profile_org, name="profile_org"),
]