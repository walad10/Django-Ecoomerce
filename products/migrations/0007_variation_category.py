# Generated by Django 3.0.2 on 2020-01-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='color', max_length=120),
        ),
    ]
