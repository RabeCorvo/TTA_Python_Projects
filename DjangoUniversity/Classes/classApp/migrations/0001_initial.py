# Generated by Django 3.1 on 2020-08-31 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.PositiveSmallIntegerField(blank=True, default='')),
                ('instructor_name', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField(blank=True, default='')),
            ],
        ),
    ]
