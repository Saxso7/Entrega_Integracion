# Generated by Django 3.2.4 on 2022-07-11 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_entrega_entregarealizada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]