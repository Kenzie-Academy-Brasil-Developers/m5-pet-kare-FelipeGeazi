from rest_framework import serializers
from traits.models import *
from rest_framework.validators import UniqueValidator
from pets.serializers import *


class TraitSerializer (serializers.Serializer):
    id=  serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(read_only=True)