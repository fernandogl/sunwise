from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView
from rest_framework import permissions, viewsets
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Url, ArchivoUrl
from .serializers import UrlSerializer, ArchivoUrlSerializer

import csv
import json


def redirige(request, codigo):
    urls = Url.objects.filter( codigo=codigo )
    if urls.exists():
        url = urls.first().original
        return HttpResponseRedirect( url )
    else:
        return HttpResponse( f'<h1>No existe una URL con este codigo: {codigo}</h1>' )


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


class UrlListView(ListView):
    model = Url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archivos'] = ArchivoUrl.objects.all()
        return context


class ArchivoUrlViewSet(viewsets.ModelViewSet):
    queryset = ArchivoUrl.objects.all()
    serializer_class = ArchivoUrlSerializer


class ArchivoUrlView(APIView):

    def post(self, request):
        file = request.FILES['upload']

        data = JSONParser().parse(file)
        archivo = ArchivoUrl.objects.create( nombre=file.name )
        for obj in data:
            obj['archivo'] = archivo.id

        url_serializer = UrlSerializer( data=data, many=True )


        if( url_serializer.is_valid() ):
            print("Es valido")
            url_serializer.save()
        else:
            print("No es valido")
            print( url_serializer.errors )
            archivo.delete()

        return Response({'received data': request.data})


def descarga_archivo_url(request, id):

    archivo = get_object_or_404( ArchivoUrl, pk=id)
    urls = Url.objects.filter( archivo=archivo )
    serializer = UrlSerializer( urls, many=True )

    data = json.dumps(serializer.data, indent=4)

    if '.' in archivo.nombre:
        nombre_archivo = archivo.nombre.split('.')[0] + '_corto.json'
    else:
        nombre_archivo = archivo.nombre

    response = HttpResponse( data, content_type='text/json')
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'

    return response





