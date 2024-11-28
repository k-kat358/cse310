# Generated by Django 5.1.3 on 2024-11-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_cuda_core_stream_processor_gpu_cuda_core_or_stream_processor'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpu',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cpucooler',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='gpu',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='mobo',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='psu',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ram',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='storage',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='case',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='CASE/'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='CPU/'),
        ),
        migrations.AlterField(
            model_name='cpucooler',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='CPUCOOLER/'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='GPU/'),
        ),
        migrations.AlterField(
            model_name='mobo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='MOBO/'),
        ),
        migrations.AlterField(
            model_name='psu',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='PSU/'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='RAM/'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Storage/'),
        ),
    ]
