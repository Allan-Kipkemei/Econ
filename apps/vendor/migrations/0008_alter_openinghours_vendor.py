# Generated by Django 3.2.4 on 2022-03-05 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_vendor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Opening', to='vendor.vendor', unique=True),
        ),
    ]