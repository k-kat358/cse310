# Generated by Django 5.1.3 on 2024-11-26 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_gpu_memory_clock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gpu',
            old_name='cuda_core_stream_processor',
            new_name='cuda_core_or_stream_processor',
        ),
    ]
