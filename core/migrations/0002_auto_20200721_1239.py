# Generated by Django 2.1.7 on 2020-07-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='org_logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
