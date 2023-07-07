from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #salvando as informações da tela
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()  
    #exibir todos os usuarios cadatrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a pagina
    return render(request, 'usuarios/usuarios.html', usuarios)