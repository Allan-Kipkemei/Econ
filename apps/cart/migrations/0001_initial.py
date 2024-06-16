# Generated by Django 3.2.4 on 2021-12-24 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=32)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.district')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village', models.CharField(max_length=32)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cell')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.district')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.sector')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.district'),
        ),
        migrations.AddField(
            model_name='cell',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.sector'),
        ),
    ]