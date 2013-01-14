# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect

from regi.news.models import News
import redis

def news(request):
    news = News.objects.all()

    return render_to_response('news.html', locals(),\
    context_instance = RequestContext(request))

def news_item(request, item_id):
    redis_db = redis.Redis(host='localhost',
                           port=6379,
                           db=0, 
                           password='')

    click_count = redis_db.incr(item_id)        
    
    news_item = News.objects.get(id=item_id)    

    return render_to_response('news_item.html', locals(),\
        context_instance = RequestContext(request))    


