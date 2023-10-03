from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('item/', views.ItemListCreate.as_view(), name='item-list-create'),
    path('item/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('carrinho/', views.CarrinhoListCreate.as_view(), name='client-list-create'),
    path('carrinho/<int:pk>/', views.CarrinhoDetail.as_view(), name='client-detail'),
    path('usuario/', views.UsuarioListCreate.as_view(), name='user-list-create'),
    path('usuario/<int:pk>', views.UsuarioDetail.as_view(), name='user-list-create'),
    path('pedido/', views.PedidoListCreate.as_view(), name='bag-list-create'),
    path('pedido/<int:pk>/', views.PedidoDetail.as_view(), name='item-detail'),
    path('webhook/', views.SimpleWebhook.as_view(), name='simple-webhook'),
]