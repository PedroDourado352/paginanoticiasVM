from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia
from .forms import NoticiaForm
# Create your views here.

def tarefas_home(request):
    contexto = {
        "nome" : "lan"
    }
    return render(request, 'tarefas/home.html', contexto)     

def tarefas_adicionar(request):
    return HttpResponse("Adicione aqui suas tarefas.") 

def noticias(request):
    return redirect('tarefas:listar_noticias')
    
def noticia_detalhe(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'tarefas/noticias/detalhe.html', {'noticia': noticia})

def criar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tarefas:listar_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'tarefas/noticias/criar.html', {'form': form})

def listar_noticias(request):
    noticias = Noticia.objects.all().order_by('-data')
    return render(request, 'tarefas/noticias/listar.html', {'noticias': noticias})

def atualizar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('tarefas:listar_noticias')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'tarefas/noticias/editar.html', {'form': form, 'noticia': noticia})

def deletar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('tarefas:listar_noticias')
    return render(request, 'tarefas/noticias/deletar.html', {'noticia': noticia})

