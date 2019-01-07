from rest_framework import serializers

from main.models import Url, ArchivoUrl


class UrlSerializer(serializers.ModelSerializer):

    codigo = serializers.ReadOnlyField()

    class Meta:
        model = Url
        fields = "__all__"


class ArchivoUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArchivoUrl
        fields = "__all__"

