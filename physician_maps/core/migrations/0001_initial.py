# Generated by Django 2.0.7 on 2018-07-17 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('zipcode', models.CharField(max_length=20, verbose_name='Zipcode')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=9, null=True)),
            ],
        ),
    ]
