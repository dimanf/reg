# -*- coding: utf-8 -*-
from django.contrib import admin
from regi.news.models import News

class NewsAdmin(admin.ModelAdmin):
    """docstring for NewsAdmin"""
    list_display = ('title', 'intro_text', 'image', 'date_create')
    list_display_links = ('title',)
    search_fields = ('title', 'intro_text', 'date_create')

admin.site.register(News, NewsAdmin)

          
