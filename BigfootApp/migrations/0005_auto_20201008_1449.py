# Generated by Django 2.2.5 on 2020-10-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigfootApp', '0004_auto_20201004_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='username',
            field=models.CharField(default='', max_length=60),
        ),
    ]
