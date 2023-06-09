from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetApp.forms import addTweetForm, addTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.
def listtweet(request):
    allTweets = models.Tweet.objects.all()
    tweetDict = {"tweets": allTweets}
    return render(request, "tweetApp/listtweet.html", context=tweetDict)
@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        message = request.POST["message"]
#        tweet = models.Tweet(nickname,message)
#        tweet.save()
        models.Tweet.objects.create(username=request.user, message=message)
        return redirect(reverse("tweetApp:listtweet"))
    return render(request, "tweetApp/addtweet.html")

def addTweetByForm(request):
    if request.method == "POST":
        form = addTweetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["nicknameInput"]
            message = form.cleaned_data["messageInput"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return(redirect(reverse("tweetApp:listtweet")))
        else:
            print("Error in FORM")
            return render(request, "tweetApp/addTweetByForm.html", context={"form": form})
    else:
        form = addTweetForm()
        return render(request, "tweetApp/addTweetByForm.html", context={"form": form})

def addTweetbyModelForm(request):
    if request.method == "POST":
        form = addTweetModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return(redirect(reverse("tweetApp:listtweet")))
        else:
            print("Error in FORM")
            return render(request, "tweetApp/addTweetByModelform.html", context={"form": form})
    else:
        form = addTweetModelForm()
        return render(request, "tweetApp/addTweetByModelform.html", context={"form": form})
@login_required
def deleteTweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect(reverse("tweetApp:listtweet"))       

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
