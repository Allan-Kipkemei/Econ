# Generated by Django 3.2.4 on 2021-12-24 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newProduct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('sector', models.CharField(max_length=100, null=True)),
                ('village', models.CharField(max_length=100, null=True)),
                ('cell', models.CharField(max_length=100, null=True)),
                ('delivery_address', models.CharField(max_length=170, null=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=13)),
                ('delivery_type', models.CharField(max_length=100, null=True)),
                ('coupon_discount', models.DecimalField(decimal_places=2, default=0, max_digits=13)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=13)),
                ('is_paid', models.BooleanField(default=False)),
                ('shipped_date', models.DateTimeField(blank=True, null=True)),
                ('arrived_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('arrived', 'Arrived')], default='ordered', max_length=20)),
                ('used_coupon', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_paid', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('is_variant', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransporterOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('ordered', 'Ordered'), ('picked', 'Picked Up'), ('delieverd', 'Delieverd')], default='ordered', max_length=20)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ordering.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='newProduct.product')),
            ],
        ),
    ]
