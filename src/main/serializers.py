from rest_framework import serializers

from main.models import Url, ArchivoUrl


class UrlSerializer(serializers.ModelSerializer):

    codigo = serializers.ReadOnlyField()
    # codigo = serializers.ReadOnlyField(source="obten_url_corta")

    class Meta:
        model = Url
        fields = ('id', 'original', 'codigo', 'archivo', 'creado')


class ArchivoUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArchivoUrl
        fields = "__all__"

