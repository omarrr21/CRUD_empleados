# Generated by Django 3.2.4 on 2021-06-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('subtitulo', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
