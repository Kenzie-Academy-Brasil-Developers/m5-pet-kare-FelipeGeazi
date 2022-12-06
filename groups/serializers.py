from rest_framework import serializers
from groups.models import *
from rest_framework.validators import UniqueValidator



class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.SerializerMethodField(max_length=50)
    created_at = serializers.DateTimeField(read_only=True)


    def scientific_name_isValid(self,scientific_name: str ) -> str:
        scientific_name_exist = Group.objects.filter(scientific_name = scientific_name).exists()

        if scientific_name_exist :
            raise serializers.ValidationError(detail="scientific_name já existe")

        return scientific_name    