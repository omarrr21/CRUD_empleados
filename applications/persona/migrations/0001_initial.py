# Generated by Django 3.2.4 on 2021-06-22 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=60, verbose_name='apellido')),
                ('job', models.CharField(choices=[('0', 'contador'), ('1', 'administrado'), ('2', 'economista'), ('3', 'otro')], max_length=5, verbose_name='trabajo')),
                ('depa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamentos')),
            ],
        ),
    ]
