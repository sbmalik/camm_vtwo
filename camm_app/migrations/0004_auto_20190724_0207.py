# Generated by Django 2.2.1 on 2019-07-24 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camm_app', '0003_paperwithref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperwithref',
            name='page',
            field=models.TextField(default='NONE'),
        ),
    ]