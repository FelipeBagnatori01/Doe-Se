from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_feed, name="show_feed"),
    path('create/', views.create_post, name="create_post")
]