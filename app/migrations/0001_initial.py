# Generated by Django 4.2.3 on 2023-08-03 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.IntegerField()),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=20)),
                ('Product_Price', models.CharField(max_length=50)),
                ('Product_Image', models.ImageField(upload_to='images')),
                ('Product_Brand', models.CharField(max_length=50, null=True)),
                ('Product_Description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slider1', models.ImageField(upload_to='slider')),
                ('Slider2', models.ImageField(upload_to='slider')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_type', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.IntegerField()),
                ('Apartment', models.CharField(max_length=50)),
                ('Society', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Zip', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
