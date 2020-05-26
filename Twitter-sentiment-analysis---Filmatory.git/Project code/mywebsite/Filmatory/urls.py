# mywebsite/Filmatory/urls.py

from django.conf.urls import url, include
from Filmatory import views

urlpatterns = [
    url(r'^$', views.HomePageView,name="home"), # Notice the URL has been named
    url(r'^tweets$', views.tweetsPageView,name="tweets"),
    url(r'^oa$', views.oaPageView,name="oa"),
    url(r'^login$',views.loginpage,name="login"),
    url(r'^logout$',views.logoutpage,name="logout"),
    url(r'^register$',views.register,name="register"),
    url(r'^search$',views.searchview,name="search"),




]
