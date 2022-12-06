from rest_framework import serializers
from pets.models import Sex, Pet
from rest_framework.validators import UniqueValidator
from traits.serializers import *
from groups.serializers import *
from groups.models import *
from traits.models import *



class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex= serializers.ChoiceField(
        choices= Sex.choices,
        default= Sex.DEFAULT,)
    group =  GroupSerializer()
    traits = TraitSerializer(many = True) 
    traits_count = serializers.SerializerMethodField(read_only=True)  


    def create(self, validated_data: dict) -> Pet: 
        group_dict = validated_data.pop("group")
        traits_list = validated_data.pop("traits")

        
        group_obj, created = Group.objects.get_or_create(
                **group_dict
            )
     
        pet_obj = Pet.objects.create(**validated_data, group = group_obj)



        for traits_dict in  traits_list:
            traits_obj, created = Trait.objects.get_or_create(
                **traits_dict
            )

            pet_obj.traits.add(traits_obj)

        
        return pet_obj 



    def get_traits_count (self, instance: Pet):

        trait_list = len(instance.traits.all())

        return trait_list



    def update(self, instance: Pet, validated_data: dict):

        group_dict: dict = validated_data.pop("group", None)
        traits_list: dict = validated_data.pop("traits", None)

        
        if group_dict: 
            group_obj, created = Group.objects.get_or_create(**group_dict)
            instance.group = group_obj  
             
              

        if traits_list:
            traits_list_instance = []
            for trait in traits_list :
              traits_obj, created = Trait.objects.get_or_create(**trait)
              traits_list_instance.append(traits_obj)


            instance.traits.set(traits_list_instance)  
            
        
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
    
        

