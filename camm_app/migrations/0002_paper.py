# Generated by Django 2.2.1 on 2019-07-19 01:56

import camm_app.JSONField
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('URL', models.TextField()),
                ('abstract', models.TextField()),
                ('container_title', models.CharField(db_column='container-title', max_length=150, verbose_name='container-title')),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('keyword', models.TextField()),
                ('page', models.CharField(max_length=20)),
                ('title', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('volume', models.CharField(max_length=20)),
                ('issued', camm_app.JSONField.JSONField(blank=True, null=True)),
                ('author', camm_app.JSONField.JSONField(blank=True, null=True)),
            ],
        ),
    ]