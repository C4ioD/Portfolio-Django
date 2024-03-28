from django.shortcuts import render
from projetos.models import Projeto

# Create your views here.
def projeto_index(request):
  projetos = Projeto.objects.all()
  context={
    'projetos':projetos
  }
  return render(request,'projetos/projetos_index.html', context)

def projeto_detalhe(request, pk):
  projeto = Projeto.objects.get(pk=pk)
  context={
    "projeto":projeto
  }
  return render(request,'projetos/projetos_detalhe.html', context)