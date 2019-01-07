from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from rest_framework import permissions, viewsets
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Url
from .serializers import UrlSerializer




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


class ArchivoUrlView(APIView):

    def post(self, request):
        file = request.FILES['upload']

        data = JSONParser().parse(file)

        # print( "NAME:", file.name )
        # print( "SIZE:", file.size )

        url_serializer = UrlSerializer( data=data, many=True )

        if( url_serializer.is_valid() ):
            print("Es valido")
            url_serializer.save()
        else:
            print("No es valido")
            print( url_serializer.errors )

        return Response({'received data': request.data})



