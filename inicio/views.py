from django.shortcuts import render


def inicio(request):
    return render(request,"inicio/inicio.html" )   
    
def usuario(request,nombre,apellido,mail,edad,genero):
    
    usuario= usuario(nombre=nombre, apellido=apellido, mail=mail, edad=edad,genero=genero )
    usuario.save()
    diccionario={
        'usuario':usuario,
    }
    return render (request,'usuario/usuario.html')