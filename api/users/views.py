from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

# Create your views here.

class LoginPage(TemplateView):
    template_name = 'login.html'
    def login(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        
        else:
            raise Exception("Nome ou usuário não encontrados")
        

class CadastroPage(TemplateView):
    template_name = 'cadastro.html'
    def cadastro(request):
        if request.session.get('usuario'):
            return redirect('/home/')
        status = request.GET.get('status')
        return render(request, 'cadastro.html', {'status': status})


    def valida_cadastro(request):
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        usuario = User.objects.filter(email = email)

        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect('/auth/cadastro/?status=1')

        if len(senha) < 8:
            return redirect('/auth/cadastro/?status=2')

        if len(usuario) > 0:
            return redirect('/auth/cadatro/?status=3')

        try:
            senha = make_password(senha)
            usuario = User(name = nome,
                            password = senha,
                            email = email)
            usuario.save()

            return redirect('/auth/cadastro/?status=0')
        except:
            return redirect('/auth/cadastro/?status=4')