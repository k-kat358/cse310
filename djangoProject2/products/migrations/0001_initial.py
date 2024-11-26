# Generated by Django 5.1.3 on 2024-11-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CASE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('case_type', models.CharField(max_length=100)),
                ('mobo_form_factor', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
                ('expansion_slots', models.CharField(max_length=100)),
                ('radiator_support', models.CharField(max_length=100)),
                ('fan_support', models.CharField(max_length=100)),
                ('storage_support', models.CharField(max_length=100)),
                ('front_panel_ports', models.CharField(max_length=100)),
                ('gpu_and_cooler_clearance', models.CharField(max_length=100)),
                ('warranty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('generation', models.CharField(max_length=100)),
                ('cores', models.IntegerField()),
                ('threads', models.IntegerField()),
                ('core_clock', models.IntegerField()),
                ('boost_clock', models.IntegerField()),
                ('cache', models.IntegerField()),
                ('power', models.FloatField()),
                ('warranty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CPUCooler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('number_of_fans', models.IntegerField()),
                ('fan_speed', models.IntegerField()),
                ('fan_airflow', models.FloatField()),
                ('noise_level', models.FloatField()),
                ('material', models.CharField(max_length=100)),
                ('dimension', models.TextField()),
                ('warranty', models.IntegerField()),
                ('power', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('chip_maker', models.CharField(max_length=100)),
                ('memory_capacity', models.IntegerField()),
                ('memory_type', models.CharField(max_length=10)),
                ('core_clock', models.CharField(max_length=100)),
                ('memory_clock', models.FloatField()),
                ('cuda_core_stream_processor', models.IntegerField()),
                ('output_ports', models.CharField(max_length=100)),
                ('dimension_weight', models.CharField(max_length=100)),
                ('other_features', models.TextField()),
                ('warranty', models.IntegerField()),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MOBO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('chipset', models.CharField(max_length=100)),
                ('mobo_form_factor', models.CharField(max_length=100)),
                ('audio_chipset', models.CharField(max_length=100)),
                ('ram_type', models.CharField(max_length=100)),
                ('ram_capacity', models.IntegerField()),
                ('ram_slot', models.IntegerField()),
                ('connector_and_ports', models.TextField()),
                ('warranty', models.IntegerField()),
                ('power', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PSU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('certification', models.CharField(max_length=100)),
                ('modular_type', models.CharField(max_length=100)),
                ('connector_types', models.TextField()),
                ('warranty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('ram_type', models.CharField(max_length=100)),
                ('ram_capacity', models.IntegerField()),
                ('ram_frequency', models.IntegerField()),
                ('operating_voltage', models.IntegerField()),
                ('cas_latency', models.CharField(max_length=100)),
                ('warranty', models.IntegerField()),
                ('power', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('storage_type', models.CharField(max_length=100)),
                ('storage_capacity', models.IntegerField()),
                ('form_factor', models.CharField(max_length=100)),
                ('speed', models.IntegerField()),
                ('interface', models.CharField(max_length=100)),
                ('warranty', models.IntegerField()),
                ('power', models.FloatField()),
            ],
        ),
    ]
