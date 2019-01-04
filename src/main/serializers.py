from rest_framework import serializers

from main.models import Url


class UrlSerializer(serializers.ModelSerializer):

    codigo = serializers.ReadOnlyField()
    
    class Meta:
        model = Url
        fields = ('id', 'original', 'codigo', 'creado')


