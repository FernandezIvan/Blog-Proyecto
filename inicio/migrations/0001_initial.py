# Generated by Django 4.2.7 on 2023-11-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=10)),
            ],
        ),
    ]
