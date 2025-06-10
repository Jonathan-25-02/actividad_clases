# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Dispositivo

def usuarios(request):
    listadoUsuarios = Usuario.objects.all()
    return render(request, "usuario.html", {'usuarios': listadoUsuarios})

def nuevoUsuario(request):
    return render(request, "nuevoUsuario.html")

def guardarUsuario(request):
    nombre = request.POST["nombre"]
    email = request.POST["email"]
    logo = request.FILES.get("logo")
    archivo = request.FILES.get("archivo")
    Usuario.objects.create(nombre=nombre, email=email, logo=logo, archivo=archivo)
    messages.success(request, "Usuario guardado exitosamente")
    return redirect('/usuarios')

def eliminarUsuario(request, id):
    Usuario.objects.get(id=id).delete()
    return redirect('/usuarios')

def editarUsuario(request, id):
    usuarioEditar = Usuario.objects.get(id=id)
    return render(request, "editarUsuario.html", {'usuarioEditar': usuarioEditar})

def procesarEdicionUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.nombre = request.POST["nombre"]
    usuario.email = request.POST["email"]
    usuario.logo = request.FILES.get("logo", usuario.logo)
    usuario.archivo = request.FILES.get("archivo", usuario.archivo)
    usuario.save()
    messages.success(request, "Usuario actualizado exitosamente")
    return redirect('/usuarios')

# asumiendo que Dispositivo tiene FK a Usuario

def dispositivos(request):
    listadoDispositivos = Dispositivo.objects.all()
    return render(request, "dispositivo.html", {'dispositivos': listadoDispositivos})

def nuevoDispositivo(request):
    usuarios = Usuario.objects.all()
    return render(request, "nuevoDispositivo.html", {'usuarios': usuarios})

def guardarDispositivo(request):
    usuario_id = request.POST["usuario"]
    tipo = request.POST["tipo"]
    sistema_operativo = request.POST["sistema_operativo"]
    modelo = request.POST["modelo"]
    fecha_autorizacion = request.POST["fecha_autorizacion"]
    logo = request.FILES.get("logo")
    archivo = request.FILES.get("archivo")

    usuario = Usuario.objects.get(id=usuario_id)

    Dispositivo.objects.create(
        usuario=usuario,
        tipo=tipo,
        sistema_operativo=sistema_operativo,
        modelo=modelo,
        fecha_autorizacion=fecha_autorizacion,
        logo=logo,
        archivo=archivo
    )

    messages.success(request, "Dispositivo guardado exitosamente")
    return redirect('/dispositivos')

def eliminarDispositivo(request, id):
    Dispositivo.objects.get(id=id).delete()
    return redirect('/dispositivos')

def editarDispositivo(request, id):
    dispositivoEditar = Dispositivo.objects.get(id=id)
    usuarios = Usuario.objects.all()
    return render(request, "editarDispositivo.html", {'dispositivoEditar': dispositivoEditar, 'usuarios': usuarios})

def procesarEdicionDispositivo(request, id):
    dispositivo = Dispositivo.objects.get(id=id)
    dispositivo.usuario = Usuario.objects.get(id=request.POST["usuario"])
    dispositivo.tipo = request.POST["tipo"]
    dispositivo.sistema_operativo = request.POST["sistema_operativo"]
    dispositivo.modelo = request.POST["modelo"]
    dispositivo.fecha_autorizacion = request.POST["fecha_autorizacion"]
    dispositivo.logo = request.FILES.get("logo", dispositivo.logo)
    dispositivo.archivo = request.FILES.get("archivo", dispositivo.archivo)
    dispositivo.save()
    messages.success(request, "Dispositivo actualizado exitosamente")
    return redirect('/dispositivos')

