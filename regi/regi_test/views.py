# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.db.models import Q

def get_user_name(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    # else:
        # return HttpResponseRedirect("/invalid/")

    return render_to_response('login.html', locals(),\
    context_instance = RequestContext(request))

def loggedin_view(request):
    return render_to_response('loggedin.html', locals(),\
    context_instance = RequestContext(request))
