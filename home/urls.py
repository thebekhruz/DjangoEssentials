from django.urls import path
from. import views

urlpatterns = [

    path("home", views.HomeView.as_view(), name="home"),
    path("authorise", views.AuthoriseView.as_view(), name="authorise")
    ]
