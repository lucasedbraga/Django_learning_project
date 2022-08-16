from django.db import models

# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self):
        return f"NOME: {self.nome} \n ( DESCRIÇÃO: {self.descricao} )"

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número") 
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    #chave estrangeira
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.numero } - Descrição: {self.descricao} ({self.campo})"


