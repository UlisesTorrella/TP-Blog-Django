# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blogito.models import Noticia, Comentario, Contacto, Categoria
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import send_mail
import smtplib
@ensure_csrf_cookie
# Create your views here.

def calculadora(request):
    context = RequestContext(request)
    return render_to_response('calculadora.html',context)

def noticias(request):
    context = RequestContext(request)
    noticias = Noticia.objects.filter(published = True)
    categorias = Categoria.objects.all()
    no_noticias=False
    if noticias.__str__()=="[]":
        no_noticias=True
    selected="Todos"
    return render_to_response('noticias.html', {'noticias':noticias,"no_noticias":no_noticias,"categorias":categorias,"seleccionado":selected}, context)

def contactanos(request):
    context = RequestContext(request)
    return render_to_response('contactanos.html', context)

def cronometro(request):
    context = RequestContext(request)
    return render_to_response('cronometro.html', context)

def curriculum(request):
    context = RequestContext(request)
    return render_to_response('curriculum.html', context)

def conversor(request):
    context = RequestContext(request)
    return render_to_response('conversor.html', context)

def imagenes(request):
    context = RequestContext(request)
    return render_to_response('imagenes.html', context)

def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)

def pregunta(request):
    context = RequestContext(request)
    return render_to_response('pregunta.html', context)

def show_post(request, id_post):
    context = RequestContext(request)
    post = Noticia.objects.get(id=id_post)
    comentarios = Comentario.objects.filter(post_id = id_post)
    return render_to_response('show_post.html',{'post':post, 'comentarios':comentarios}, context)

def mensaje(request):
    context = RequestContext(request)
    if request.method == 'POST':
        #ESTO OBTIENE LOS DATOS QUE VIENEN EL EL "HTTP POST" NO TIENE NADA QUE VER CON LOS MODELS NAADAADADADA 
        nombre= request.POST.get('nombre')
        mensaje= request.POST.get('mensaje')
        id_post= request.POST.get('id')
        #-------------------------------------
        #ACA CREAS UN MODEL Y LE METES LOS DATOS QUE CONSEGUIMOS ANTES, ANTES ME REFIERO A LO DE ARRIBA
        comentario = Comentario()
        comentario.autor = nombre
        comentario.mensaje = mensaje
        comentario.post_id = id_post
        #ACA GUARDAMOS EL COMENTARIO QUE CREAMOS
        comentario.save()
    
    #ACA FILTRAMOS TODOS LOS COMENTARIOS QUE PERTENEZCAN AL POST QUE ESTAMOS VIENDO PARA PASARSELO 
    id_post= request.POST.get('id')
    comentarios = Comentario.objects.filter(post_id = id_post)
    return render_to_response('mensajes.html',{'comentarios':comentarios}, context)

def mail(request):
    context = RequestContext(request)
    if request.method == 'POST':
        #Guarda el contacto en la base de datos... por que si
        mail= request.POST.get('mail')
        mensaje= request.POST.get('mensaje')
        asunto= request.POST.get('asunto')
        contacto = Contacto()
        contacto.asunto = asunto
        contacto.mail = mail
        contacto.mensaje = mensaje
        contacto.save()
        #Para enviar Mail ami mismo diciendo como asunto quien lo manda y sobre que y en el contenido lo que el usuario dice
        username = "matidemayi@gmail.com"
        password = "rewstrew"
        fromaddr = "matidemayi@gmail.com"
        toaddr = "matidemayi@gmail.com"
        msg = "Subject: Mensaje de "+mail+", Sobre: "+asunto+"\n\n"+mensaje
        server = smtplib.SMTP_SSL('smtp.googlemail.com:465')
        server.login(username, password)
        server.sendmail(fromaddr, [toaddr], msg)
        server.quit()

    return render_to_response('contactanos.html', context)

def show_categoria(request, id_categoria):
    print "entro"
    context = RequestContext(request)
    noticias = Noticia.objects.filter(published = True, categoria=id_categoria)
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.filter(id=id_categoria)
    no_noticias=False
    if noticias.__str__()=="[]":
        no_noticias=True
    return render_to_response('noticias.html', {'noticias':noticias,"no_noticias":no_noticias,"categorias":categorias,"selected":categoria}, context)
