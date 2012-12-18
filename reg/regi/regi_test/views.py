# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.db.models import Q

def get_user_name(request):
    return render_to_response('base.html', locals(),\
    context_instance = RequestContext(request))
