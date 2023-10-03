from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Classe que define o modelo item
class Item(models.Model):
    nome = models.CharField(max_length=80)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'item'

    def __str__(self):
        return '%d: %s' % (self.id, self.nome)

# Classe que define o modelo usuário
class Usuario(AbstractUser):
    def __str__(self):
        return self.username

# Classe que define o modelo carrinho
class Carrinho(models.Model):
    nome = models.CharField(max_length=80)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carrinho'

    def __str__(self):
        return '%d: %s' % (self.id, self.nome)

# Classe que define o modelo pedido
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    itens = models.ManyToManyField('Item')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    dt_compra = models.DateField(auto_now=True)

    class Meta:
        db_table = 'pedido'

    def __str__(self):
        return '%d' % (self.id)
