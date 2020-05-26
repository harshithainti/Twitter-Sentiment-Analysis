# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import csv
import sys
from django.shortcuts import render, HttpResponse, redirect
import re
import tweepy
from importlib import reload
from textblob import TextBlob
from .forms import Searchform
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import CreateUserForm
from .models import MovieNames

# Create your views here.


# Add the two views we have been talking about  all this time :)


def loginpage(request):
    next=request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            if next:
                return redirect('login')
            return redirect('home')
        else:
            messages.info(request,'User name or password is incorrect')

    context={}
    return render(request,'login.html')
@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')

def register(request):
    form=CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account has been created for '+user)
            return redirect('login')

    context={'form':form}
    return render(request,'register.html',context )

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def HomePageView(request):
    consumer_key = "OycHbv63os98XA1WqRJbB9lT4"
    consumer_secret = "aWt2CjULqrnnKe4gdVkI6yBwqeyzOgoqQwzfOlvJ9LmkZtTO1z"
    access_token = "1235206685477793792-xxnYDEZiN6Tv82DRjJNRkM1ByKAPKv"
    access_token_secret = "9VE6g8JpdWC7YKRKgH6qBaDEGQEPL4qjWmy4WXww2hdB0"
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)

    if request.method == 'POST':
        searchform = Searchform(request.POST)
        if searchform.is_valid():
            searchtext='%s' %(searchform.cleaned_data['search'])
            searchform.save()

            #get the name of the spreadsheet we will write to
            fname = '_'.join(re.findall(r"#(\w+)", searchtext))

            #open the spreadsheet we will write to
            with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/tweets.csv', 'w') as file:

                w = csv.writer(file)

                #write header row to spreadsheet
                w.writerow(['tweet_text'])

                #for each tweet matching our hashtags, write relevant info to the spreadsheet
                for tweet in tweepy.Cursor(api.search, q=searchtext+' -filter:retweets', \
                                           lang="en", tweet_mode='extended').items(100):
                    w.writerow([tweet.full_text.replace('\n',' ').encode('utf-8')])

            form = Searchform()
            return render(request,'index.html',{'searchform':form, 'searchitem':searchtext})

        else:
            form = Searchform()
            return render(request,'index.html',{'searchform':form})



    else:
        form = Searchform()
        return render(request,'index.html',{'searchform':form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def tweetsPageView(request):
    #reload(sys)

    #sys.setdefaultencoding('utf-8')
    with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/tweets.csv','r') as read_file:
        csv_reader=csv.reader(read_file)
        list1=[]
        next(csv_reader)
        for line in csv_reader:
            line=str([cell.encode('utf-8') for cell in line])
            list1.append(line)
        positive=0
        negative=0
        neutral=0
        positive_tweets=[]
        negative_tweets=[]
        neutral_tweets=[]
        for line in list1:
            analysis=TextBlob(line)
            if(analysis.sentiment.polarity>0):
                positive+=1
                positive_tweets.append(line)
            elif(analysis.sentiment.polarity<0):
                negative+=1
                negative_tweets.append(line)
            elif(analysis.sentiment.polarity==0):
                neutral+=1
                neutral_tweets.append(line)

        with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/reviews.csv', 'w') as file:
            w = csv.writer(file)
            #write header row to spreadsheet
            w.writerow([positive])
            w.writerow([negative])
            w.writerow([neutral])

    return render(request,'tweets.html',{'pt1':positive_tweets[0],'pt2':positive_tweets[1],'pt3':positive_tweets[2],'pt4':positive_tweets[3],'pt5':positive_tweets[4],'pt6':positive_tweets[5],'pt7':positive_tweets[6],'pt8':positive_tweets[7],'pt9':positive_tweets[8],'pt10':positive_tweets[9],'pt11':positive_tweets[10],'pt12':positive_tweets[11],'pt13':positive_tweets[12],'pt14':positive_tweets[13],'pt15':positive_tweets[14],'pt16':positive_tweets[15],'pt17':positive_tweets[16],'pt18':positive_tweets[17],'pt19':positive_tweets[18],'pt20':positive_tweets[19],'ngt1':negative_tweets[0],'ngt2':negative_tweets[1],'ngt3':negative_tweets[2],'ngt4':negative_tweets[3],'ngt5':negative_tweets[4],'ngt6':negative_tweets[5],'ngt7':negative_tweets[6],'ngt8':negative_tweets[7],'ngt9':negative_tweets[8],'ngt10':negative_tweets[9],'ngt11':negative_tweets[10],'ngt12':negative_tweets[11],'ngt13':negative_tweets[12],'ngt14':negative_tweets[13],'ngt15':negative_tweets[14],'ngt16':negative_tweets[15],'ngt17':negative_tweets[16],'ngt18':negative_tweets[17],'ngt19':negative_tweets[18],'ngt20':negative_tweets[19],'nt1':neutral_tweets[0],'nt2':neutral_tweets[1],'nt3':neutral_tweets[2],'nt4':neutral_tweets[3],'nt5':neutral_tweets[4],'nt6':neutral_tweets[5],'nt7':neutral_tweets[6],'nt8':neutral_tweets[7],'nt9':neutral_tweets[8],'nt10':neutral_tweets[9],'nt11':neutral_tweets[10],'nt12':neutral_tweets[11],'nt13':neutral_tweets[12],'nt14':neutral_tweets[13],'nt15':neutral_tweets[14],'nt16':neutral_tweets[15],'nt17':neutral_tweets[16],'nt18':neutral_tweets[17],'nt19':neutral_tweets[18],'nt20':neutral_tweets[19],})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def oaPageView(request):
    list1=[]
    with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/reviews.csv','r') as read_file:
            csv_reader=csv.reader(read_file)
            for line in csv_reader:
                    list1.append(line)
            goodlist=list1[0]
            badlist=list1[1]
            avglist=list1[2]
            good=""
            bad=""
            avg=""
            for i in goodlist:
                good+=i
            for i in badlist:
                bad+=i
            for i in avglist:
                avg+=i
            good=int(good)
            bad=int(bad)
            avg=int(avg)


    return render(request,'oa.html',{'positive':good, 'negative':bad,'neutral':avg})


def searchview(request):
    posts=MovieNames.objects.all()
    users=User.objects.all()
    return render(request,'search.html',{'post':posts,'user':users})
