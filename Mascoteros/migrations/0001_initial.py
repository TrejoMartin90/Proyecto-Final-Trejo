# Generated by Django 4.1.5 on 2023-02-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=64)),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to='images')),
                ('tamaño', models.CharField(max_length=32)),
                ('apto_niños', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('direccion', models.CharField(max_length=255)),
                ('horario', models.CharField(max_length=64)),
                ('imagen', models.ImageField(upload_to='images')),
                ('descripcion', models.CharField(max_length=500)),
                ('pagina_web', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to='images')),
                ('especie_objetivo', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=32)),
            ],
        ),
    ]
