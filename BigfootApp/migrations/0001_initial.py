# Generated by Django 2.2.5 on 2020-10-02 21:42
# Generated by Django 2.2.5 on 2020-10-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=60, unique=True)),
                ('street', models.CharField(default='', max_length=180, verbose_name='Nearest Street Address')),
                ('city', models.CharField(default='', max_length=100, verbose_name='Nearest City')),
                ('state', models.CharField(max_length=80, verbose_name='State or Province')),
                ('postal_code', models.CharField(default='', max_length=10, verbose_name='Postal Code')),
                ('country', models.CharField(choices=[('Canada', 'Canada'), ('USA', 'United States')], max_length=60)),
                ('enc_date', models.DateField(max_length=20, verbose_name='Encounter Date')),
                ('description', models.TextField(blank=True, max_length=600, verbose_name='Brief Description Of Encounter')),
                ('enc_visual', models.BooleanField(default=False, verbose_name='Was This A Visual Encounter?')),
            ],
        ),
    ]
