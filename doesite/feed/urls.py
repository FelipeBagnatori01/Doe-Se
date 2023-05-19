from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.show_feed, name="show_feed"),
    path('create/', views.create_post, name="create_post"),
    path('organization/', views.show_feed_org, name="show_feed_org"),
    path('config/', views.config, name="config"),
    path('login/', views.login, name="login"),
    path('', views.landing, name="landing"),
]