# Generated by Django 2.0.2 on 2018-04-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_newsselectmodel_donga'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsselectmodel',
            name='hani',
            field=models.BooleanField(default=True, verbose_name='한겨레'),
        ),
    ]
