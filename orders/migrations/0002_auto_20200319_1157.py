# Generated by Django 3.0.2 on 2020-03-19 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10000),
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10000),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10000),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]