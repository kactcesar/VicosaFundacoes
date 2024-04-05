
from rest_framework import serializers
from.models import*


class CategoriaPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPessoa
        fields = '__all__'  
        
        
class CategoriaImpactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaImpacto
        fields = '__all__'  
        

class CategoriaStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriaStatus
        fields = '__all__'  