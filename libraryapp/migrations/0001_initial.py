# Generated by Django 4.0.3 on 2022-04-19 06:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.IntegerField()),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('is_active', models.IntegerField(null=True)),
            ],
            managers=[
                ('admin_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
