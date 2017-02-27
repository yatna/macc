#Version : Phython/Django 2.7.6, PostgreSQL 9.3.4
#Author : Vaibhavi Desai
#Github username : desaivaibhavi
#email : ranihaileydesai@gmail.com

import datetime
import uuid

import jinja2
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Min, Sum
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from jinja2.ext import loopcontrols

from signup.models import *

jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

#Checker function used to see if user is logged in and verified etc. Made separately instead of writing repeatedly
def check(request):
    
    #Check if user is logged in
    if not request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":None}))

    #Check if user has an associated rider
    #(This will be false if the admin logs in)
    try:
        request.user.pcuser
    except:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'<p>No Pcuser associated! Add a pcuser from admin</p>'}))
    
    return None 
