# Generated by Django 3.0.5 on 2020-05-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200512_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposition',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
