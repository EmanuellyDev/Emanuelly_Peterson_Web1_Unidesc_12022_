# Generated by Django 4.0.4 on 2022-06-23 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(max_length=100)),
                ('dadosCliente', models.CharField(max_length=100)),
                ('dadosCorretor', models.CharField(max_length=100)),
                ('descricaoImovel', models.CharField(max_length=100)),
                ('documentacao', models.CharField(max_length=100)),
                ('clausulaPenal', models.CharField(max_length=100)),
            ],
        ),
    ]
