# Generated by Django 3.1.7 on 2021-03-01 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0006_pontoturistico_enderecos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
        ),
    ]
