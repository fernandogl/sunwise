from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from rest_framework import permissions, viewsets

from .models import Url
from .serializers import UrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated, )

    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


def redirige(request, codigo):
	urls = Url.objects.filter( codigo=codigo )
	if urls.exists():
		url = urls.first().original
		return HttpResponseRedirect( url )
	else:
		return HttpResponse( f'No existe una URL con este codigo: {codigo}' )



class UrlListView(ListView):
    model = Url