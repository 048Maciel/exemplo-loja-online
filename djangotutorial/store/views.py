from django.shortcuts import render
from .models import Artigo, Categoria, Vendedor


def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, "lista_artigos.html", {"artigos": artigos})


def artigos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    artigos = Artigo.objects.filter(categoria=categoria)
    return render(request, "categoria.html", {
        "categoria": categoria,
        "artigos": artigos
    })


def perfil_vendedor(request, vendedor_id):
    vendedor = Vendedor.objects.get(id=vendedor_id)
    artigos = Artigo.objects.filter(vendedor=vendedor)
    return render(request, "vendedor.html", {
        "vendedor": vendedor,
        "artigos": artigos
    })
from django.shortcuts import render
from .models import Artigo

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, "lista.html", {"artigos": artigos})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Store a funcionar 🚀")

from django.shortcuts import render
from .models import Artigo

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, "store/lista.html", {"artigos": artigos})