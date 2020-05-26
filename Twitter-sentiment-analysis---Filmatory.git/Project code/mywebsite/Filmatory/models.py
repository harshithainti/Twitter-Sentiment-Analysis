# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class MovieNames(models.Model):
    search = models.CharField(max_length=20,null=True)
    datefi = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.search
