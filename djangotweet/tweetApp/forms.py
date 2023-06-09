from django import forms
from django.forms import TextInput,Textarea, ModelForm
from tweetApp.models import Tweet


class addTweetForm(forms.Form):
    nicknameInput = forms.CharField(label="Nickname", max_length=50, widget=forms.TextInput(
        attrs={
            'placeholder': 'Name', 
            'style': 'width: 300px;', 
            'class': 'form-control'
            }
            ))
    messageInput = forms.CharField(label="Message", max_length=200, widget=forms.Textarea(attrs={
        'placeholder': "Message",
        "class": "form-control"

    }))

class addTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username", "message"]