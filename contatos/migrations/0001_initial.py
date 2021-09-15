# Generated by Django 3.2.7 on 2021-09-14 22:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('data_cricao', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria')),
            ],
        ),
    ]
