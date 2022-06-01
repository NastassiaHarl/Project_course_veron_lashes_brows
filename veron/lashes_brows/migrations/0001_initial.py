# Generated by Django 4.0.4 on 2022-06-01 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('info_of_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=255)),
                ('info_service', models.CharField(max_length=255)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lashes_brows.master')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lashes_brows.service')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lashes_brows.service')),
            ],
        ),
        migrations.CreateModel(
            name='Gift_certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_certificate', models.ImageField(upload_to='')),
                ('stock', models.CharField(max_length=255)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lashes_brows.master')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lashes_brows.master')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_map', models.ImageField(upload_to='')),
                ('info_address', models.CharField(max_length=255)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lashes_brows.master')),
            ],
        ),
    ]
