from django.contrib import admin
from tweetApp.models import Tweet

# Register your models here.
class tweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message', {"fields":["message"]}),
        ('Nickname', {"fields":["nickname"]})
    ]
    #fields = ["nickname","message"]
admin.site.register(Tweet, tweetAdmin)

