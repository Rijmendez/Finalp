# Generated by Django 4.0.6 on 2022-09-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=40)),
                ('stock', models.CharField(max_length=40)),
                ('precio', models.CharField(max_length=40)),
                ('cantidad', models.CharField(max_length=40)),
                ('totalapagar', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'factura',
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'formulario',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=40)),
                ('cantidad', models.CharField(max_length=40)),
                ('stock', models.CharField(max_length=40)),
                ('precio', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Registropp',
            },
        ),
    ]