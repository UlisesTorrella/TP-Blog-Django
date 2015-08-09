# -*- coding: utf-8 -*-
from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calculadora/$', views.calculadora, name='calculadora'),
    url(r'^contactanos/$', views.contactanos, name='contactanos'),
    url(r'^cronometro/$', views.cronometro, name='cronometro'),
    url(r'^pregunta/$', views.pregunta, name='pregunta'),
    url(r'^imagenes/$', views.imagenes, name='imagenes'),
    url(r'^curriculum/$', views.curriculum, name='curriculum'),
    url(r'^conversor/$', views.conversor, name='conversor'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^show_post/(?P<id_post>[0-9]+)/$', 'blogito.views.show_post', name='show_post'),
    url(r'^mensaje/$', 'blogito.views.mensaje', name='mensaje'),
    url(r'^mail/$', 'blogito.views.mail', name='mail'),
    url(r'^show_categoria/(?P<id_categoria>[0-9]+)/$', 'blogito.views.show_categoria', name='show_categoria'),
]