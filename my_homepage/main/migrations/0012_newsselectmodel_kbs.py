# Generated by Django 2.0.2 on 2018-04-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_newsselectmodel_khan'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsselectmodel',
            name='kbs',
            field=models.BooleanField(default=True, verbose_name='kbs'),
        ),
    ]
