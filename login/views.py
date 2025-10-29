from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Usuario, UsuarioRol, Rol

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(username=username, password=password, estado=1)

            usuario_rol = UsuarioRol.objects.filter(id_usuario=usuario.id_usuario).first()
            rol = Rol.objects.get(id_rol=usuario_rol.id_rol) if usuario_rol else None

            #request.session['usuario_id'] = usuario.id_usuario
            #request.session['username'] = usuario.username
            #request.session['rol'] = rol.nombre

            return redirect('lista_aromas')
        except Usuario.DoesNotExist:
            messages.error(request, 'Credenciales inválidas')
            return render(request, 'login/login.html')

    return render(request, 'login/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('/')