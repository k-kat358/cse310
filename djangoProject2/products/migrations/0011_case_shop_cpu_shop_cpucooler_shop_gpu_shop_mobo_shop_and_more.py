# Generated by Django 5.1.3 on 2024-11-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_case_price_cpu_price_cpucooler_price_gpu_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
        migrations.AddField(
            model_name='cpu',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
        migrations.AddField(
            model_name='cpucooler',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
        migrations.AddField(
            model_name='gpu',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
        migrations.AddField(
            model_name='mobo',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
        migrations.AddField(
            model_name='psu',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
        migrations.AddField(
            model_name='ram',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
        migrations.AddField(
            model_name='storage',
            name='shop',
            field=models.CharField(default='Default Shop', max_length=100),
        ),
    ]
