# Generated by Django 2.0.2 on 2018-04-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180420_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pres', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Daum',
        ),
        migrations.DeleteModel(
            name='Naver',
        ),
    ]
