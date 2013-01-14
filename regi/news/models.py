# -*- coding: utf-8 -*-
from django.db import models
from djangosphinx.models import SphinxSearch
from tinymce.models import HTMLField

class News(models.Model):
    """ Класс новостей """
    title = models.CharField(u'заголовок', max_length=50)
    intro_text = models.TextField(u'вступительный текст')
    main_text = models.TextField(u'текст', blank=True)   
    image = HTMLField(u'Изображение') 
    date_create = models.DateTimeField(u'дата создания')
    date_update = models.DateTimeField(u'дата последнего обновления', auto_now=True)

    my_search = SphinxSearch(
        options = {
            'realtime': True,

            'included_fields': [
                'text',
                'bool',
                'uint',
            ],
            'excluded_fields': [
                'excluded_field2',
            ],
            'stored_attributes': [
                'stored_string',
                'datetime',
            ],
            'stored_fields': [
                'stored_string2',
            ],
            'related_fields': [
                'related_field',
                'related_field2',

                'city__title',
            ],
            'mva_fields': {
                'm2m_field',
            },
        },
        query_options = {
            'ranker':'proximity_bm25',
            'reverse_scan':True,
        },
        snippets = True,
        snippets_options = {
            'before_match':'<span class="snippet">',
            'after_match':'</span>',
        }
        # maxmatches = 2000,
        # limit = 100,
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости' 
        
