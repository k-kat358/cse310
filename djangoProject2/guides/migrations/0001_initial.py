# Generated by Django 5.1.2 on 2024-12-03 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cpu', models.TextField()),
                ('cpu_cooler', models.TextField()),
                ('motherboard', models.TextField()),
                ('memory', models.TextField()),
                ('storage', models.TextField()),
                ('gpu', models.TextField()),
                ('psu', models.TextField()),
                ('case', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GuidesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.CharField(choices=[('CPU', 'CPU'), ('CPU Cooler', 'CPU Cooler'), ('Motherboard', 'Motherboard'), ('Memory', 'Memory'), ('Storage', 'Storage'), ('GPU', 'GPU'), ('PSU', 'PSU'), ('Case', 'Case')], max_length=50)),
                ('image', models.ImageField(upload_to='guides/images/')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='guides.guides')),
            ],
        ),
    ]
