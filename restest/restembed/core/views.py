from django.shortcuts import render

from django.conf import settings

import requests
import json

from .forms import SubmitEmbed
#from .serializer import EmbedSerializer

def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            #print('Nombre: ', nombre)
            # Invocación POST enviando nombre como raw
            #r = requests.post('http://localhost:8001/idealweight/', data = nombre)
            m = json.dumps(nombre)
            #r = requests.post('http://localhost:8001/holamundo/', data = nombre)
            r = requests.post('http://localhost:8001/holamundo/', data = m)
            jsonr = r.json()
            # DEBUG -> BORRAR
            #print(jsonr)
#            serializer = EmbedSerializer(data=json)
#            if serializer.is_valid():
#                embed = serializer.save()
#                return render(request, 'embeds.html', {'embed': embed})
            return render(request, 'embeds.html', {'embed': jsonr})
    else:
        form = SubmitEmbed()

    return render(request, 'index.html', {'form': form})
