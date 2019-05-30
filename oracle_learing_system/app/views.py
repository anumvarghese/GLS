# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

import datetime
import json

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader

def home(request):
    context = {} 
    return render(request, 'index.html', context)

