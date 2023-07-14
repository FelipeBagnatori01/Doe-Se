from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.show_feed, name="show_feed"),
    path('feed_org/', views.show_feed_org, name="show_feed_org"),
    path('create/', views.create_post, name="create_post"),
    path('organization/', views.show_feed_org, name="show_feed_org"),
    path('config/', views.config, name="config"),
    path('login_org/', views.login_org, name="login_org"),
    path('', views.landing, name="landing"),
    path('create_account/', views.create_account, name="create_account"),
    path('create_institution/', views.create_institution, name="create_institution"),
    path('profile/', views.profile, name="profile"),
    path('profile_org/', views.profile_org, name="profile_org"),
    path('account_created/', views.users, name="account_created"),
    path('institution_created/', views.institutes, name="institution_created"),
    path('user_logged/', views.user_login, name="user_logged"),
    path('institution_logged/', views.institution_login, name="institution_logged"),
    path('upload/', views.upload, name="upload"),
]