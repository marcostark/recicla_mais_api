from django.db import models


class RecyclingCompany(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=255)
    thumb = models.CharField(verbose_name='URL da imagem', max_length=255)
    address = models.CharField(verbose_name='Endereço', max_length=255)
    phone = models.CharField(verbose_name='Telefone', max_length=255)
    description = models.CharField(verbose_name='Descrição', max_length=255)
    lat = models.CharField(verbose_name='Latitude', max_length=50)
    lon = models.CharField(verbose_name='Longitude', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Empresa de Reciclagem'
        verbose_name_plural = 'Empresas de Reciclagem'

        # O
        # que
        # recebe
        # Embalagem
        # longa
        # vidaEmbalagem
        # longa
        # vida
        # MetaisMetais
        # Papel
        # brancoPapel
        # branco
        # PlásticoPlástico
        # VidroVidro


class CollectionPoints(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=255)
    thumb = models.CharField(verbose_name='URL da imagem', max_length=255)
    description = models.CharField(verbose_name='Descrição', max_length=255)
    materials = models.CharField(verbose_name='Materiais Recolhidos', max_length=255)
    lat = models.CharField(verbose_name='Latitude', max_length=50)
    lon = models.CharField(verbose_name='Longitude', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ponto de Coleta'
        verbose_name_plural = 'Pontos de Coleta'


class CollectsNeighborhoods(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=255)
    days = models.CharField(verbose_name='Dia da Semana', max_length=255)
    schedule = models.TimeField(verbose_name='Hora da Coleta')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Horário'
        verbose_name_plural = 'Horarios'