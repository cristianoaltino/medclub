from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import *

# Create your views here.
class SimpleWebhook(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        pass
        print(request.data)
        return Response({}, status=status.HTTP_200_OK)

# Classe usada para listar e criar itens
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

# Classe usada para atualizar e remover item
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        return super(ItemDetail, self).destroy(request, *args, **kwargs)

# Classe usada para listar e criar carrinho de itens
class CarrinhoListCreate(generics.ListCreateAPIView):
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Carrinho.objects.filter(usuario=user.pk)

# Classe usada para atualizar e remover o carrinho de itens
class CarrinhoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Carrinho.objects.filter(usuario=user.pk)

    def destroy(self, request, *args, **kwargs):
        return super(CarrinhoDetail, self).destroy(request, *args, **kwargs)

# Classe usada para listar usuário
class UsuarioListCreate(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Usuario.objects.all()
        return Usuario.objects.filter(id=user.pk)

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Usuario.objects.all()
        return Usuario.objects.filter(id=user.pk)

# Classe usada para litar e criar pedido
class PedidoListCreate(generics.ListCreateAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Pedido.objects.all()
        return Pedido.objects.filter(usuario__id=user.pk)

# Classe usada para atualizar e remover pedido
class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Pedido.objects.filter(usuario__id=user.pk)

    def destroy(self, request, *args, **kwargs):
        return super(PedidoDetail, self).destroy(request, *args, **kwargs)
