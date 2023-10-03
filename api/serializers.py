from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
    Item, Carrinho, Usuario, Pedido
)

# Create your serializers here.

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id','nome','valor']

class CarrinhoSerializer(serializers.ModelSerializer):
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Carrinho
        fields = ['id','nome', 'usuario']

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuario
        fields = ['id','username','first_name','last_name','email','password']

    def create(self, data):
        data['password'] = make_password(data.get('password'))
        return super(UsuarioSerializer, self).create(data)

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedido
        fields = ['id','usuario','carrinho','itens','valor_total','dt_compra']
