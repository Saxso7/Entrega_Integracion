# Generated by Django 4.0.5 on 2022-07-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=60)),
                ('nroSeguimiento', models.CharField(max_length=10)),
                ('producto', models.CharField(max_length=20)),
                ('cantidad', models.CharField(max_length=2)),
                ('precio', models.CharField(max_length=8)),
                ('entregaRealizada', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=60)),
                ('nroSeguimiento', models.CharField(max_length=10)),
                ('producto', models.CharField(max_length=20)),
                ('cantidad', models.CharField(max_length=2)),
                ('precio', models.CharField(max_length=8)),
            ],
        ),
    ]