# Generated by Django 5.0.3 on 2024-03-12 04:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Application Name')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='View Name')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='rest_authorization.application')),
            ],
            options={
                'verbose_name': 'View',
                'verbose_name_plural': 'Views',
                'db_table': 'view',
            },
        ),
        migrations.CreateModel(
            name='ActionMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Action Name')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('put', 'PUT'), ('patch', 'PATCH'), ('delete', 'DELETE')], max_length=10, verbose_name='Action Method')),
                ('url_pattern', models.CharField(max_length=200, verbose_name='URL Pattern')),
                ('users', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_rest_auth_set', related_query_name='user_rest_auth', to=settings.AUTH_USER_MODEL, verbose_name='Users Rest API Permissible')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='rest_authorization.view')),
            ],
            options={
                'verbose_name': 'Action Method',
                'verbose_name_plural': 'Action Methods',
                'db_table': 'action_method',
            },
        ),
    ]