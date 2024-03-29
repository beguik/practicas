# Generated by Django 2.2.12 on 2022-02-07 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMarca', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreModelo', models.CharField(max_length=30)),
                ('agnoModelo', models.DateField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroCoches.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('matricula', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=15)),
                ('kilometros', models.IntegerField(default=0)),
                ('agnoMatriculacion', models.DateField()),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroCoches.Modelo')),
            ],
        ),
    ]
