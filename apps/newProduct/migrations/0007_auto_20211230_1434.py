# Generated by Django 3.2.4 on 2021-12-30 14:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newProduct', '0006_alter_product_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='detail',
        ),
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
