from ctypes import resize
from rest_framework import serializers
from apps.coordinador.models import Coordinador

from apps.semillero_app.apis.serializers import SemilleroSerializer


class CoordinadorSerializer(serializers.ModelSerializer):
    semillerolist = SemilleroSerializer(many=True, read_only=True)

    class Meta:
        model = Coordinador
        fields = "__all__"


class CoordinadorUserSerializer(serializers.ModelSerializer):
    # semillerolist = SemilleroSerializer(many=True, read_only=True)

    class Meta:
        model = Coordinador
        fields = [
            "n_identificacion",
            "nombre",
            "f_nacimiento",
            "lugar_expedicion",
            "lugar_nacimiento",
            "celular",
            "email",
            "direcccion",
            "c_emergencia",
            "n_emergencia",
            "create_at",
        ]
