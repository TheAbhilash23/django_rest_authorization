# Generated by Django 5.0.3 on 2024-03-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('publication_year', models.PositiveIntegerField()),
                ('rating', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Book Category',
                'verbose_name_plural': 'Book Categories',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('production_year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Car Model',
                'verbose_name_plural': 'Car Models',
            },
        ),
    ]