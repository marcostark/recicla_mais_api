# Generated by Django 2.2.6 on 2019-10-07 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('thumb', models.CharField(max_length=255, verbose_name='URL da imagem')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('lat', models.CharField(max_length=50, verbose_name='Latitude')),
                ('lon', models.CharField(max_length=15, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Ponto de Coleta',
                'verbose_name_plural': 'Pontos de Coleta',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CollectsNeighborhoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('days', models.CharField(max_length=255, verbose_name='Dia da Semana')),
                ('schedule', models.TimeField(verbose_name='Hora da Coleta')),
            ],
            options={
                'verbose_name': 'Horário',
                'verbose_name_plural': 'Horarios',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RecyclingCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('thumb', models.CharField(max_length=255, verbose_name='URL da imagem')),
                ('address', models.CharField(max_length=255, verbose_name='Endereço')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('lat', models.CharField(max_length=50, verbose_name='Latitude')),
                ('lon', models.CharField(max_length=15, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Empresa de Reciclagem',
                'verbose_name_plural': 'Empresas de Reciclagem',
                'ordering': ['-id'],
            },
        ),
    ]
