# Generated by Django 2.0.2 on 2018-04-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180430_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsselectmodel',
            name='donga',
            field=models.BooleanField(default=True, verbose_name='동아일보'),
        ),
    ]