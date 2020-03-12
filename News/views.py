# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Novidade



def home(request):
    context = {
        "text": "goutemberg@icloud.com",
        "nomes": ["gouberg@gmail.com", "goutemberg@icloud.com", "carol@icloud.com"]
    }
    return render (request, "index.html", context)

def contato(request):
    context = {}
    return render(request, "contato.html", context)

def novidades_detalhes(request):
    obj = Novidade.objects.get(id=1)
    context = {
        "objects": obj
    }
    return render(request, "novidades.html", context)

