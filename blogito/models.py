# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Noticia(models.Model):
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering=['-fecha']
    titulo = models.CharField(u"Titulo",max_length=200)
    noticia = models.TextField(u"Noticia")
    descripcion = models.TextField(u"Descripcion")
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    categoria = models.ManyToManyField('Categoria')
    published = models.BooleanField(u'Publicado?', default=True)
    autor = models.ForeignKey(User)
    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
    asunto = models.CharField(u'asunto', max_length=100)
    mail = models.CharField(u'Mail', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    def __str__(self):
        return self.mail

class Categoria(models.Model):
    nombre = models.CharField(u'Título de la Categoría', max_length=100)
    descripcion = models.CharField(u'Descripción de la Categoría', max_length=256)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering=['-fecha']
    autor = models.CharField(u'Nombre', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    post = models.ForeignKey(Noticia)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    def __str__(self):
        return self.autor
