# Generated by Django 2.0.2 on 2018-05-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_newsselectmodel_sbs'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsselectmodel',
            name='mbc',
            field=models.BooleanField(default=True, verbose_name='mbc'),
        ),
    ]
