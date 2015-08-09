# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Noticia, Contacto, Comentario, Categoria
# Register your models here.
admin.site.register(Noticia)
admin.site.register(Contacto)
admin.site.register(Comentario)
admin.site.register(Categoria)
