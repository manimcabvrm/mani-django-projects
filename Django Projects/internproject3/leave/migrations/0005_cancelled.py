# Generated by Django 2.2 on 2020-03-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0004_auto_20200304_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancelled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('date_and_time', models.CharField(max_length=20)),
            ],
        ),
    ]
