from django.urls import path
from . import views
app_name = "tweetApp"
urlpatterns = [
    path("", views.listtweet, name="listtweet"),
    path("addtweet/", views.addtweet, name="addtweet"),
    path("addTweetByForm/", views.addTweetByForm, name="addTweetByForm"),
    path("addTweetModelForm/", views.addTweetbyModelForm, name="addTweetByModelform"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("delete/<int:id>", views.deleteTweet, name="deletetweet")
]