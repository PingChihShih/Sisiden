# Generated by Django 2.0.6 on 2018-06-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180612_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleorder',
            name='sugar',
            field=models.CharField(choices=[('normal', '正常糖'), ('little', '少糖'), ('no', '無糖')], max_length=4),
        ),
    ]
